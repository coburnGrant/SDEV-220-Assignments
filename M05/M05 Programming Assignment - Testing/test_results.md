## Describe the test results in your own words.  What do the test results mean?

Looking at the test results, we can see that our test_list_int test succeeds, while, our test_list_fraction test fails.
When running the test we an `AssertionError: Fraction(9, 10) != 1`. This is correct, 9/10 does not equal 1. 

Looking at our test implementation we pass in the fractions: 1/4 + 1/4 + 2/5 to our sum function. 
Doing same manual desk checking, we can see that the sum of those fractions is indeed 9/10, and not 1 like we assert it will in our test.

So thankfully, our actual implementation of the sum function is not flawed, and it is our logic of our tests.
To fix our test, we would need to change that assertion to be the correct value: `Fraction(9, 10)`.
