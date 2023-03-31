# this will be an app to replicate what is being made by Mobile+Web in
# Android. The idea is to concept and deploy for the practice

import functions_pyc

time_vars = 2023

week_punch_comtainer = []

# testing variables
mon_p_in = functions_pyc.time_func_args(2023, 3, 20, 7, 00, 00)
mon_l_out = functions_pyc.time_func_args(2023, 3, 20, 12, 00, 00)
mon_l_in = functions_pyc.time_func_args(2023, 3, 20, 12, 30, 00)
mon_p_out = functions_pyc.time_func_args(2023, 3, 20, 16, 30, 00)

tue = functions_pyc.time_func_args(2023, 3, 21, 7, 00, 00)

wed = functions_pyc.time_func_args(2023, 3, 22, 7, 00, 00)

thur = functions_pyc.time_func_args(2023, 3, 23, 7, 00, 00)

fri = functions_pyc.time_func_args(2023, 3, 24, 7, 00, 00)

print(functions_pyc.punch_in())
print(functions_pyc.time_func_args(time_vars, 3, 20, 7, 00, 00))
print((mon_l_out - mon_p_in))
print((mon_p_out - mon_l_in))
