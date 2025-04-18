## Describe the test results in your own words.  What do the test results mean?

### Basic tests

Our `test_sum` test succeeds meaning our sum function handles basic sum of an array

Our `test_sum_2` tests have the same test as the previous file, which still succeeds, as well as a new test that sums values from a tuple, which fails. 
Looking at the test results, this is because we assert that the sum of a tuple with the values 1, 2, 2 has a sum of 6, which is incorrect as it has a sum of 5. To fix our test, we would need to change one of the values in the tuple to be increased by 1 or assert that the sum will equal 5.

### `unittest` Tests

Our `test_sum_unittest` script has the same tests as the previous script, but just using the `unittest` library. We get the same results from the previous test script with the first one passing, and the second test failing, because our tests have the same issues.

### Project tests

Looking at the test results from our project directory, we can see that our `test_list_int` test succeeds, while, our `test_list_fraction` test fails.
When running the test we an `AssertionError: Fraction(9, 10) != 1`. This is correct, 9/10 does not equal 1. 

Looking at our test implementation we pass in the fractions: 1/4 + 1/4 + 2/5 to our sum function. 
Doing same manual desk checking, we can see that the sum of those fractions is indeed 9/10, and not 1 like we assert it will in our test.

So thankfully, our actual implementation of the sum function is not flawed, and it is our logic of our tests.
To fix our test, we would need to change that assertion to be the correct value: `Fraction(9, 10)`.
