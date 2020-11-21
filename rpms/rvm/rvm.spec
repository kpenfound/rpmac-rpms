Name:       rvm
Version:    1.29.10
Release:    1%{?dist}
Summary:    Ruby enVironment Manager
License:    Apache
URL:        https://github.com/rvm/rvm

Source0:    https://github.com/rvm/rvm/archive/%{version}.tar.gz

%description
Ruby enVironment Manager (RVM)

%prep

%build
%{?exp_env}
%{?env_options}

%install
%{?env_options}
%{__mkdir_p} %{buildroot%}%{_bindir}
%{__install} -m0755 %{buildroot}%{_bindir}/rvm

%files
%{_bindir}/rvm

%changelog
* Sat Nov 21 2020 Kyle Penfound <kpenfound11@gmail.com> - 1.29.10-1
- Initial RPM Commit
