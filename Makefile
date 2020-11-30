SPECDIRS=./rpms
REPOPATH=mac/x86_64/
RPMS=$(shell ls ./rpms)

define create_rpm
	rpmbuild --undefine=_disable_source_fetch -bb $(abspath $(SPECDIRS)/$(1)/$(1).spec);
endef


.PHONY: repo
repo:
	$(foreach dir,$(RPMS),$(call create_rpm,$(dir)))
