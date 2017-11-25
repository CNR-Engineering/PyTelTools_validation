BASH_SCRIPTS=$(wildcard */out.sh)

ROOT_PATH=/home/lucd/Public/BOULOT/DEV_PYTHON

OUT_FOLDERS=$(shell find ./* -name 'out' -type d)

out: $(foreach script,$(BASH_SCRIPTS),$(dir $(script))out)
test: $(foreach script,$(BASH_SCRIPTS),$(dir $(script))test)

%/out: %/out.sh
	@echo "===== RUNNING $(shell dirname $<) ====="
	mkdir -p $@
	cd $(dir $<) && ./out.sh

%/test: %/out
	@echo "===== TESTING $(shell dirname $<) ====="
	@cd $(dir $<) && diff -x "*.dbf" out ref

clean:
	rm -rf $(OUT_FOLDERS)

.PHONY: clean out
