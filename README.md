<h1>Colorfan</h1>
<p>Colorfan is a powerful Python module that allows you to set console colors in your Python applications. With this module, you can add color and style to the text displayed on the terminal/command prompt.</p>
<p>This module was created by Hamidreza Ahmadi and is available on his GitHub page under the username <a href="https://github.com/hushra">hushra</a>. You can find the source code, documentation, and examples on his page.</p>
<h2>Installation</h2>
<p>To install Colorfan, you can use pip:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body ">pip <span class="hljs-keyword">install</span> colorfan
</code></pre>
<h2>Usage</h2>
<p>To use Colorfan, you can import the module and use its functions as shown in the following example:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span></div><code class="hljs code-block-body "><span class="hljs-keyword">import</span> colorfan
<span class="hljs-built_in">print</span>(colorfan.colorize(<span class="hljs-number">255</span>, [<span class="hljs-number">100</span>],<span class="hljs-number">1</span>) + <span class="hljs-string">"hi"</span>)
</code></pre>
<p>In this example, the <code>colorize()</code> function is used to print "hi" in a specific color with a weight of 1. The <code>fgcolor()</code> and <code>bgcolor()</code> functions can also be used to set the foreground and background colors separately, and the <code>uncolor()</code> function can be used to reset the console color to its default setting.</p>
<h2>Functions</h2>
<p>The following functions are available in the Colorfan module:</p>
<ul>
<li><code>colorize(fgcolor, bgcolor, weight=0)</code>: Returns the color code for a specific combination of foreground and background colors with a specified weight.</li>
<li><code>fgcolor(fgcolor)</code>: Returns the color code for a specific foreground color.</li>
<li><code>bgcolor(bgcolor)</code>: Returns the color code for a specific background color.</li>
<li><code>uncolor()</code>: Resets the console color to its default setting.</li>
</ul>
<h2>Input Formats</h2>
<p>The following functions are available in this module:</p>
<ul>
<li><code>colorize</code></li>
<li><code>fgcolor</code></li>
<li><code>bgcolor</code></li>
<li><code>uncolor</code></li>
</ul>
<h3><code>colorize</code></h3>
<p>The <code>colorize</code> function takes three arguments: <code>fgcolor</code>, <code>bgcolor</code>, and <code>weight</code>.</p>
<p>The <code>fgcolor</code> and <code>bgcolor</code> arguments specify the foreground and background colors for the output text, respectively. These arguments can be either RGB values or color names.</p>


<p>Accepted RGB values are arrays of three integers representing the red, green, and blue values for the desired color.</p>
<p>The <code>weight</code> argument specifies the weight (or intensity) of the text. It should be an integer between 0 and 99, with higher values indicating bolder text. The default value is 0.</p>
<h3><code>fgcolor</code> and <code>bgcolor</code></h3>
<p>These functions are simpler versions of <code>colorize</code>. They each take one argument, which is the color for the foreground or background, respectively. The format of this argument is the same as for <code>fgcolor</code> and <code>bgcolor</code> in <code>colorize</code>.</p>
<h3><code>uncolor</code></h3>
<p>The <code>uncolor</code> function returns the escape code to reset the terminal color back to its default value.</p>
<ul>
<li><code>colorize</code></li>
<li><code>fgcolor</code></li>
<li><code>bgcolor</code></li>
<li><code>uncolor</code></li>
</ul>
<h3>Predetermined color</h2>
<p>These variables are values that you can call predefined colors by calling them:</p>
<ul>
<li><code>red = [205,0,0]
green = [0,205,0]
white = [255,255,255]
black = [0,0,0]
gray = [50,50,50]
blue = [0,0,205]
yellow = [255, 230, 0]
magenra = [255,0,255]
cyan = [0,255,255]</code></li>
</ul>
<p>For more information on how to use these functions, please refer to the documentation on Hamidreza Ahmadi's GitHub page.</p>
<h2>Conclusion</h2>
<p>With Colorfan, you can easily add color and style to the text displayed on the terminal/command prompt in your Python applications. This module is easy to use and highly customizable, making it a great choice for developers who want to create eye-catching console interfaces.</p>
