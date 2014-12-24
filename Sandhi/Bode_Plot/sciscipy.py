import sciscipy 
import scilab
code_string1 = "s = %s;"
code_string2 = "Gc = syslin('c'," + str(2*1) + "*s + " + str(2) + "*s^2 + 1," + str(3) + "*s);"
code_string3 = "r = tf2ss(Gc);"
code_string4 = "u = " + str(3) + ";"
code_string5 = "y = csim(u,1:length(u),r)"
code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string5
sciscipy.eval(code_string)
y = sciscipy.read("y")