%bcond_with check
%bcond_with snapshot

%global goipath         sigs.k8s.io/kind
%global forgeurl	https://github.com/kubernetes-sigs/kind


%if %{with snapshot}
%global commit          ee165688557465ff456077293061f344b05b130f
%gometa
Version:                0
Release:        	2%{?dist}
%else
%global tag             v0.10.0
Version:                0.10.0
%gometa
Release:        	1%{?dist}
%endif

%global common_description %{expand:
Kubernetes IN Docker - local clusters for testing Kubernetes.}

%global golicenses      LICENSE
%global godocs          README.md OWNERS

Name:           kind
Summary:        Kubernetes IN Docker - local clusters for testing Kubernetes

License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang >= 1.14

# HACK: These aren't correctly resolving or need to be packaged in copr.
BuildRequires: golang(github.com/golangci/lint-1)
BuildRequires: golang(github.com/alessio/shellescape)
BuildRequires: golang-gotest-devel
BuildRequires: golang-k8s-code-generator

BuildRequires:  golang(github.com/alessio/shellescape)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/coreos/go-iptables/iptables)
BuildRequires:  golang(github.com/evanphx/json-patch/v5)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(github.com/vishvananda/netlink/nl)
BuildRequires:  golang(gopkg.in/yaml.v3)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/version)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/klog)
BuildRequires:  golang(k8s.io/utils/net)

%if %{with check}
BuildRequires: podman
BuildRequires: systemd
%endif


%description
%{common_description}

%gopkg

%prep
%goprep


%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/kind %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Disabling due to Docker deps. Will revist.
%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE %{golicenses}
%doc code-of-conduct.md CONTRIBUTING.md README.md
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Jan 24 22:57:00 EST 2021 Daniel Gadd <fedora@gadd.co.nz> - 0.10.0-1
- Inital v0.10.0 release