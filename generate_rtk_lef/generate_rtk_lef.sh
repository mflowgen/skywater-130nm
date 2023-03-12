# Script for generating LEF file
# Author: Charles Tsao

# Generate LEF
cp $SKYWATER130_HOME/libs.ref/sky130_fd_sc_hd/techlef/sky130_fd_sc_hd__nom.tlef \
    $TOP/view-standard/rtk-tech.lef

# Edit LEF per issue #308 and #312
sed -i '/END pwell/ a \
\
LAYER poly\
  TYPE MASTERSLICE ;\
END poly\
\
LAYER licon1\
  TYPE CUT ;\
\
  WIDTH 0.17 ;                # Licon 1\
  SPACING 0.17 ;              # Licon 2\
  ENCLOSURE BELOW 0 0 ;       # Licon 4\
  ENCLOSURE ABOVE 0.08 0.08 ; # Poly / Met1 4 / Met1 5\
END licon1' $TOP/view-standard/rtk-tech.lef

sed -i '/END met5/ a \
\
LAYER OVERLAP\
  TYPE OVERLAP ;\
END OVERLAP' $TOP/view-standard/rtk-tech.lef

