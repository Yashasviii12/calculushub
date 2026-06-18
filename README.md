<h1>CALCULUS HUB</h1>
<h2> GRAPH ANALYSER: </h2>
 <p> About: This tool enables you to make graphs of different functions and tells you the points of discontinuity and non-differentiability as an output.</p>
 <br>
<p>Algorithm of the project:</p>
<br>
1. user enters the function in the form of a string.<br>
2. string gets converted to a mathematical expression using sympy.<br>
3. Find discontinuity, like where function is undefined and store these points in a set. <br>
4. Apply symbolic differentiation rules to find f'(x).<br>
5. make a set of non differentiable points and take the union with the set of discontinuity. <br>
6. plot the graph of the function using numpy and matplotlib. <br>
