Name:           kubecolor
Version:        0.0.20
Release:        0%{?dist}
Summary:        Colorize your kubectl output

License:        ASL 2.0
URL:            https://github.com/dty1er/kubecolor
Source0:        https://github.com/dty1er/kubecolor/releases/download/v%{version}/kubecolor_%{version}_Linux_x86_64.tar.gz

%description
Colorize your kubectl output

%prep
%autosetup -n %{name} -c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -p -m 755 %{name} %{buildroot}/usr/bin

%files
/usr/bin/kubecolor

%changelog
* Tue Feb 09 2021 Daniel Gadd <fedora@gadd.co.nz>
- Inital RPM