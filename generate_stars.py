"""
A coding problem from the U******y interview.
Use console to output the stars:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

if __name__ == "__main__":

    for i in range(5):
        print(f"{' '*(4-i)}{'*'*(2*i+1)}")

    for i in range(3, -1, -1):
        print(f"{' '*(4-i)}{'*'*(2*i+1)}")
