Name:       #NAME#
Version:    1
Release:    1
Summary:    #SUMMARY#
License:    #LICENSE#
URL:        #URL#

Source0:    #SOURCE0#

%description
#DESCRIPTION#

%prep
#PREP#

%build
%{?exp_env}
%{?env_options}
#BUILD#

%install
%{?env_options}
#INSTALL#

%files
#FILES#

%changelog
