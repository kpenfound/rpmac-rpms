Name:       nvm
Version:    0.37.0
Release:    1%{?dist}
Summary:    Node Version Manager
License:    MIT
URL:        https://github.com/nvm-sh/nvm

Source0:    https://github.com/nvm-sh/nvm/archive/v%{version}.tar.gz

%description
Node Version Manager - POSIX-compliant bash script
to manage multiple active node.js versions

%prep
%setup -n nvm-%{version}

%build
%{?exp_env}
%{?env_options}

%install
%{?env_options}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0755 nvm.sh %{buildroot}%{_bindir}
%{__install} -m0755 nvm-exec %{buildroot}%{_bindir}

%post
if [ "$1" = 1 ]; then
    echo 'Add the following to ~/.bash_profile or your desired shell configuration file:\n
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm'
fi

%files
%{license} LICENSE.md
%{_bindir}/nvm.sh
%{_bindir}/nvm-exec

%changelog
* Wed Nov 18 2020 Kyle Penfound <kpenfound11@gmail.com> - 0.37.0-1
- Initial RPM Commit
