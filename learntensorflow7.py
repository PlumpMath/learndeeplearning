import tensorflow as tf 

'''
In order to change the value of the variable, you 
can use the variable.assign() method, which gives
the variable the new value to be. Note that 
Variable.assign() is an Operation, and must be
run in a Session to take effect:
'''

# Create variable with starting value of 1
my_var = tf.Variable(1)
my_const = tf.constant(2, name="my_const")

# Create an operation that multiplies the 
# variable by 2 each time it is run 
my_var_times_two = my_var.assign(tf.mul(my_var,my_const))

# Initialization operation
init = tf.global_variables_initializer()

# Start a session
with tf.Session() as sess:
	sess.run(init)

	#Multiply variable by two and return it
	sess.run(my_var_times_two)
	# Out: 2

	sess.run(my_var_times_two)
	# Out: 4

	print(sess.run(my_var_times_two))
	# Out: 8

	writer = tf.summary.FileWriter("./my_graph4", sess.graph)
	writer.close()

	sess.close()






