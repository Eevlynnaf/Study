/*
Datatypes
int
The int data type is used for variables that will store integers
integers always take up 4 bytes of memory (32bits). This means the range of values they can store is necessarily to 32 bits worth o information
integer range:
-2^31 -> 0 -> +2^31 -1
half for negative numbers and half for positive numbers

unsigned int
unsigned is a qualifier that can be applied to certain types(including int)
which effectively doubles the positive range of variables of that type
at the cost of disallowing any negative values
unsigned int range:
0 ->  2^32 -1


char
the char data type is used for variables that will store single characters
characters always take up 1 byte of memory (8bits)
this means the range of values they can store is necessarily limited to 8 bits worth of information
thanks to ASCII we've developed a mapping of characters like A, B, C... to numeric values in the positive side of this range
char range:
-128 -> 127

float
the float data type is used for variables that will store floating-point values, also known as real numbers
floating point values always take up 4 bytes of memory (32bits)
it's complicated to describe the range of a float, but suffice it to say with 32 bits of precision, some of which might be used
for an integer part, we are limited in how precise we can be

double
the double data type is used for variables that will store floating-point values, also known as real numbers
the difference is that doubles are double precision
they always take up 8 bytes of memory (64bits)
with an additional 32 bits of precision relative to a float, doubles allow to specify much more precise real numbers

void
is a type, not a data type
functions can have a void return type, which just means they don't return a value
the parameter list of a function can also be void, it simply means the function takes no parameters
think of void as a placeholder for nothing

bool
the bool data type is used for variables that will store a boolean value
more precisely, they are capable of only storing one of two values: true and false


















*/