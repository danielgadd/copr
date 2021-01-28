Name:           kfctl
Version:        1.2.0
Release:        1%{?dist}
Summary:        A tool to control and manage Kubeflow deployments

License:        ASL 2.0
URL:            https://github.com/kubeflow/kfctl
Source0:        https://github.com/kubeflow/%{name}/releases/download/v%{version}/%{name}_v%{version}-0-gbc038f9_linux.tar.gz

%description
A tool to control and manage Kubeflow deployments

%prep
%autosetup -n %{name} -c


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
install -p -m 755 %{name} %{buildroot}/usr/bin

%files
/usr/bin/kfctl

%changelog
* Thu Jan 28 2021 Daniel Gadd <fedora@gadd.co.nz>
- Inital RPM