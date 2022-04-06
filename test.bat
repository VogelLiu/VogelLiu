sed -i "s#<td>Anforderung</td>#<td bgcolor=\"\#66ffcc\">Anforderung<\/td>#g" csv2html_sbs.html

sed -i "s#<td>1\.#<td bgcolor=\"\#ff0000\"><strong>1\.#g" csv2html_sbs.html
sed -i "s#<td>2\.#<td bgcolor=\"\#800000\"><strong>2\.#g" csv2html_sbs.html
sed -i "s#<td>3\.#<td bgcolor=\"\#ffff00\"><strong>3\.#g" csv2html_sbs.html
sed -i "s#<td>4\.#<td bgcolor=\"\#808000\"><strong>4\.#g" csv2html_sbs.html
sed -i "s#<td>5\.#<td bgcolor=\"\#00ff00\"><strong>5\.#g" csv2html_sbs.html
sed -i "s#<td>6\.#<td bgcolor=\"\#008000\"><strong>6\.#g" csv2html_sbs.html
sed -i "s#<td>7\.#<td bgcolor=\"\#00ffff\"><strong>7\.#g" csv2html_sbs.html
sed -i "s#<td>8\.#<td bgcolor=\"\#008080\"><strong>8\.#g" csv2html_sbs.html
sed -i "s#<td>9\.#<td bgcolor=\"\#0000ff\"><strong>9\.#g" csv2html_sbs.html

sed -i "s#<td>QM#<td bgcolor=\"\#ff1234\">QM#g" csv2html_sbs.html

sed -i "s#\\\r\\\n#<br>#g" csv2html_sbs.html
