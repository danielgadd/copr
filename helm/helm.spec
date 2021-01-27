Name:           helm
Version:        3.5.0
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager

License:        Apache
URL:            https://helm.sh/
Source0:        https://get.helm.sh/%{name}-v%{version}-linux-amd64.tar.gz

%description
The Kubernetes Package Manager

%prep
%autosetup -n %{name} -c


%install
#rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -p -m 755 linux-amd64/%{name} %{buildroot}/usr/bin

%files
/usr/bin/helm
