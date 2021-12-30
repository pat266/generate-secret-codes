# generate-secret-codes

About: The algorithm can produce n-amount of genereated codes with m-amount of length (200 and 6 by default respectively). If there is already a `code.csv` file, it will add more codes to it as appropriately. It uses the `secrets` library to get each code in order to guarantee the randomness when choosing each letter/digit. <br /><br />

Why: My sister asked me to generate about 100 unique codes to be used as a personal discount code for her product (https://academy.beactiveiseasy.com/), so I made this so that she can easily get more codes when she need it. <br /><br />

Possible Cons:<br />
1. If the input number of code to be generated < number of code in the .csv file, it will do nothing. This is to ensure that the generated codes do not get lost.<br />

All arguments/changable variables:  <br />
* `path`: The path to the directory where `code.csv` is saved
* `length`: the length of each code
* `num`: the number of code to be saved in the `code.csv` file