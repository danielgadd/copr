Name:           helm
Version:        3.5.1
Release:        0%{?dist}
Summary:        The Kubernetes Package Manager

License:        ASL 2.0
URL:            https://helm.sh/
Source0:        https://get.helm.sh/%{name}-v%{version}-linux-amd64.tar.gz

%description
The Kubernetes Package Manager

%prep
%autosetup -n %{name} -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -p -m 755 linux-amd64/%{name} %{buildroot}/usr/bin

%files
/usr/bin/helm

%changelog
* Thu Jan 28 2021 Daniel Gadd <fedora@gadd.co.nz>
- Inital RPM