<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
          "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8">
<title> analisys.py </title>
<link rel="shortcut icon" href="http://www.python.org/favicon.ico">
<style type="text/css">
.comment {color: crimson;}
.definition {color: darkorange; font-weight:bold;}
.defname {color: blue;}
.docstring {color: forestgreen; font-style:italic;}
.builtin {color: purple;}
.operator {color: brown;}
.keyword {color: darkorange;}
.string {color: forestgreen;}
</style>
</head>
<body><pre class="python">
<span class="docstring">'''Show how powerful list comprehensions are for testing and data analysis


    Syntax for a set comprehension:
        { &lt;expr&gt; for &lt;var&gt; in &lt;interable&gt; if &lt;cond&gt; }

    Syntax for a list comprehension:
        [ &lt;expr&gt; for &lt;var&gt; in &lt;interable&gt; if &lt;cond&gt; ]

'''</span>

<span class="definition">import</span> portfolio
<span class="definition">from</span> pprint <span class="definition">import</span> pprint

port <span class="operator">=</span> portfolio.get_portfolio(<span class="string">'notes/stocks.txt'</span>)

<span class="builtin">print</span>(<span class="string">'Projections ==Looking at a subset of the columns'</span>)
<span class="builtin">print</span>([trade.symbol <span class="keyword">for</span> trade <span class="keyword">in</span> port])
<span class="builtin">print</span>([trade.shares <span class="keyword">for</span> trade <span class="keyword">in</span> port])
<span class="builtin">print</span>([trade.price <span class="keyword">for</span> trade <span class="keyword">in</span> port])
<span class="builtin">print</span>()

<span class="builtin">print</span>(<span class="string">'How many shares of Cisco have you purchase cumulatively?'</span>)
<span class="builtin">print</span>(<span class="string">'SELECT SUM(shares) FROM Port WHERE symbol = "CSCO";'</span>)
<span class="builtin">print</span>(<span class="builtin">sum</span>([trade.shares <span class="keyword">for</span> trade <span class="keyword">in</span> port <span class="keyword">if</span> trade.symbol <span class="operator">==</span> <span class="string">'CSCO'</span>]))

<span class="builtin">print</span>(<span class="string">'Make an alphabetical list of the companies you have traded'</span>)
<span class="builtin">print</span>(<span class="string">'SELECT DISCTINCT symbol FROM Port ORDER BY symbol;'</span>)
<span class="builtin">print</span>(<span class="builtin">sorted</span>({trade.symbol <span class="keyword">for</span> trade <span class="keyword">in</span> port}))

</pre>

</body>
</html>
