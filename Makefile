SPECDIRS=./rpms
REPOSUBDIR=mac
RPMDIR=rpmbuild/RPMS
RPMS=$(shell ls ./rpms)

define create_rpm
	rpmbuild --undefine=_disable_source_fetch -bb $(abspath $(SPECDIRS)/$(1)/$(1).spec);
endef


.PHONY: repo
repo:
	$(foreach dir,$(RPMS),$(call create_rpm,$(dir)))
	mkdir tmprepo
	aws s3 sync ${REPO_BUCKET} ./tmprepo/
	cp -r ${HOME}/${RPMDIR} ./tmprepo/${REPOSUBDIR}
	docker run -v $(abspath ./tmprepo/$(REPOSUBDIR)/x86_64):/data sark/createrepo:latest
	aws s3 sync --acl=public-read --delete ./tmprepo/ ${REPO_BUCKET}
	rm -r tmprepo
