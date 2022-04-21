Gate-level VCS simulation fails with the error message ``Identifier 'SET' has not been declared yet. If this error is not expected, please check if you have set \`default_nettype to none.`` Temporarily fixing the issue by removing those statements from `primitives.v` using `generate_verilog.sh`.
   ```
   sed -i 's/`default_nettype none//g' view-standard/primitives.v
   ```
