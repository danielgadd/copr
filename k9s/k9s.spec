Name:           k9s
Version:        0.24.13
Release:        0%{?dist}
Summary:        Kubernetes CLI To Manage Your Clusters In Style!
License:        ASL 2.0
URL:            https://k9scli.io/
Source0: https://github.com/derailed/k9s/releases/download/v%{version}/k9s_v%{version}_Linux_x86_64.tar.gz

# there's no debug files in this build
%define debug_package %{nil}

%description
K9s provides a terminal UI to interact with your Kubernetes clusters.
The aim of this project is to make it easier to navigate, observe and
manage your applications in the wild. K9s continually watches
Kubernetes for changes and offers subsequent commands to
interact with your observed resources.

%prep
%autosetup -n %{name} -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -p -m 755 %{name} %{buildroot}/usr/bin

%files
/usr/bin/k9s

%changelog
* Thu Jan 28 2021 Daniel Gadd <fedora@gadd.co.nz>
- Inital RPM