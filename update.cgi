#!/bin/bash
cat<<EOF
Content-Type: text/html

<html>
<head>
<title>Updating</title>
</head>
<body>
<p>
END

date
git pull origin master

cat<<EOF
<pre>
</pre>
</body>
</html>
EOF