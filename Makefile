# Makefile for auto-generating skywater-130nm-adk
# Author: Charles Tsao


.PHONY: adk
all adk: rtk_lef captable lib sc_lef spi cdl verilog \
	db milkyway gds magic

.PHONY: rtk_lef
rtk_lef:
	-@./generate_rtk_lef/generate_rtk_lef.sh

.PHONY: captable
captable:
	cd generate_captable && ./generate_captable.sh && cd ../

.PHONY: lib
lib:
	cd generate_lib && ./generate_lib.sh && cd ../

.PHONY: sc_lef
sc_lef:
	-@./generate_sc_lef/generate_sc_lef.sh

.PHONY: spi
spi:
	-@./generate_spi/generate_spi.sh

.PHONY: cdl
cdl:
	-@./generate_cdl/generate_cdl.sh

.PHONY: verilog
verilog:
	-@./generate_verilog/generate_verilog.sh

.PHONY: db
db: lib
	cd generate_db && ./generate_db.sh && cd ../

.PHONY: milkyway
milkyway:
	cd generate_milkyway && ./generate_milkyway.sh && cd ../
	
.PHONY: gds
gds:
	-@./generate_gds/generate_gds.sh

.PHONY: magic
magic:
	-@./generate_magic_files.sh

.PHONY: clean
clean:
	-@find 'view-standard' -mindepth 1 -maxdepth 1 ! -name 'adk.tcl' ! -name 'rtk-stream-out.map' -exec rm -rv {} +

