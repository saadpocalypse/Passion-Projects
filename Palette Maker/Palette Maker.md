# Palette Maker

## How it works
* I made this application using HTML, JavaScript and Bootstrap 5. 
* There are 6 columns, each with their individual color and a button at the bottom. 
* Clicking on the button calls the _setBG()_ function which requires the column ID and the _\<h4\>_ tag ID as arguments.
* The function generates a random number between 000000 and 16777215. The function then converts this number to its equivalent hexadecimal value which ranges between 000000 and FFFFFF, which are the minimum and maximum values on the hexadecimal scale of color.
* This number is given a _'#'_ as a prefix and the resulting string is set as the background color of the column and it also replaces the content inside the _\<h4\>_ tag in question.
* The _copyDivToClipboard()_ function copies the content inside the _\<h4\>_ tag, which is the hexadecimal value of the column color, to the clipboard. It takes the ID of the _\<h4\>_ tag as an argument.

## How to use
* Click on the _switch_ button under a column to change the column's color.
* Click on the column to copy its hexadecimal value.