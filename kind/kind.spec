Name:           kind
Version:        0.11.1
Release:        0%{?dist}
Summary:        kind is a tool for running Kubernetes clusters using Docker

License:        ASL 2.0
URL:            https://kind.sigs.k8s.io/
Source0:        https://kind.sigs.k8s.io/dl/v%{version}/kind-linux-amd64


%description
kind is a tool for running local Kubernetes clusters
using Docker container “nodes”.
kind was primarily designed for testing Kubernetes itself,
but may be used for local development or CI.

%prep
%autosetup -n %{name} -c -T

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -p -m 755 %{SOURCE0} %{buildroot}/usr/bin/kind

%files
/usr/bin/kind

%changelog
* Thu Feb 4 2021 Daniel Gadd <fedora@gadd.co.nz>
- Inital RPM