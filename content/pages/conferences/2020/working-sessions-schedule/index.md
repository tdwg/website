---
title: Schedule of Working Sessions,  September 21-25
summary: 
cover_image: https://static.tdwg.org/conferences/2020/ConferenceImage-CR.jpg
cover_image_by: 
cover_image_ref: 
tags: conference
page_order: 45
---
<script type="text/javascript"> 

function horaLocal(hileraFechaHora) {
  var fecha = new Date(hileraFechaHora);   // The function convert the parameter ISO Date string to the local hour HH:MM.
  var horas = fecha.getHours();
  var minutos = fecha.getMinutes();
  
  if (horas < 10) {
     horas = "0" + horas.toString();
  }
  if (minutos < 10) {
     minutos = "0" + minutos.toString();
  }
  return horas + ":" + minutos;
}

function UTCLocal(hileraFechaHora) {
  var fecha = new Date(hileraFechaHora);    // The function convert the parameter ISO Date string to the UTC shift.
  var desfase = (0-fecha.getTimezoneOffset())/60;
  if (desfase > 0) {
     desfase = "+" + desfase.toString();
  } else {
     desfase = desfase.toString();
  }
  return "UTC"+desfase;
}

function DiaLocal(hileraFechaHora, lineas, formatoDia, formatoMes, localidad) {
  // The function convert the parameter ISO Date string to the day string.
  // lineas indicates if the result is more than 1 line (No:0, Yes:1)
  var fecha = new Date(hileraFechaHora);
  var nombreDia = fecha.toLocaleDateString(localidad, { weekday: formatoDia });
  var nombreMes = fecha.toLocaleDateString(localidad, { month: formatoMes });
  if (lineas = 1) {
    nombreDia = nombreDia + "<br>";
  } else {
    nombreDia = nombreDia + " ";
  }
  nombreDia = nombreDia + fecha.getDate() + " " + nombreMes;
  return nombreDia;
}
</script>
# Schedule of Working Sessions<br />21-25 September

<table>
<tr> 
	<td>Latest news</td>
	<td style="text-align: right;">26 Sep, 2020 </td>
</tr>
<tr> 
	<td colspan=2><p>The working sessions of TDWG 2020 were held in the week of 21-25 September. These included the Introduction to TDWG, interest group, task group, and birds-of-a-feather meetings, as well as workshops and a hackathon.  If you missed a session, you can watch the recorded video on the TDWG YouTube channel.  A link to each session's video is listed in the table below.</p>
	</td>
</tr>
</table>
<p>&nbsp;</p>
<table border="1">
<thead>
<tr style="border-style: double;">
<td style="background-color: #cccccc; vertical-align: bottom;">
<script type="text/javascript">
  document.write( UTCLocal('2020-09-21T08:00:00Z') );
</script>
</td>
<td style="background-color: #99aacc; text-align: center;">
  <script type="text/javascript">
    document.write( DiaLocal('2020-09-21T08:00:00Z', 1, 'short', 'short', 'en-US') );
  </script>
</td>
<td style="background-color: #99aacc; text-align: center;">
  <script type="text/javascript">
    document.write( DiaLocal('2020-09-22T08:00:00Z', 1, 'short', 'short', 'en-US') );
  </script>
</td>
<td style="background-color: #99aacc; text-align: center;">
  <script type="text/javascript">
    document.write( DiaLocal('2020-09-23T08:00:00Z', 1, 'short', 'short', 'en-US') );
  </script>
</td>
  <td style="background-color: #99aacc; text-align: center;"><script type="text/javascript">
    document.write( DiaLocal('2020-09-24T08:00:00Z', 1, 'short', 'short', 'en-US') );
  </script>
</td>
<td style="background-color: #99aacc; text-align: center;">
  <script type="text/javascript">
    document.write( DiaLocal('2020-09-25T08:00:00Z', 1, 'short', 'short', 'en-US') );
  </script>
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
<script type="text/javascript">
  document.write( horaLocal('2020-09-21T08:00:00Z') );
</script>
</td>
<td> </td>
<td style="background-color: #e6ffaa;" rowspan="4">
  <p><a href="../working-sessions/#itg07:%20how%20did%20it%20die?">ITG07: How Did It Die?</a>
  <p>Primary: Sophia Ratcliffe</p>
  <p>Support: Quentin Groom</p>
  <p><a href="https://youtu.be/tsWXd1LWXbI" target="_blank" title="ITG07: How Did It Die?">Recorded Video</a></p>
</td>
<td style="background-color: #bbffaa;" rowspan="4">
  <p><a href="../working-sessions/#hack01:%20hack4nature">HACK01: Hack4Nature</a></p>
  <p>Primary: Olivier Rovellotti</p>
  <p><a href="https://youtu.be/xYvTEnqtGdQ" target="_blank" title="HACK01: Hack4Nature">Recorded Video</a><p></p>
</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T08:30:00Z') );
</script>
</td>
<td style="background-color: #ffeeaa;" rowspan="3">
	<p><a href="../working-sessions/#intro:%20introduction%20to%20tdwg">INTRO: Introduction to TDWG</a></p>
	<p>Primary: Holly Little</p>
	<p>Support: Deb Paul</p>
	<p><a href="https://youtu.be/2btF029nSiI" target="_blank" title="INTRO: Introduction to TDWG (1)">Recorded Video</a></p>
</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
<script type="text/javascript">
    document.write( horaLocal('2020-09-21T09:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
<script type="text/javascript">
  document.write( horaLocal('2020-09-21T09:30:00Z') );
</script>
</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T10:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td style="background-color: #aaffc3;" rowspan="4">
	<p><a href="../working-sessions/#itg09:%20people%20in%20biodiversity%20data%20task%20group">ITG09: People in Biodiv</a></p>
	<p>Primary: David Shorthouse</p>
	<p>Support: Quentin Groom</p>
	<p><a href="https://youtu.be/DiulnUoY2SI" target="_blank" title="ITG09: People in Biodiversity">Recorded Video</a><p></p>
</td>
<td> </td>
</tr>
<tr>
<td>10:30
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T10:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T11:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T11:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
  <td>
    <script type="text/javascript">
      document.write( horaLocal('2020-09-21T12:00:00Z') );
    </script>
</td>
<td style="background-color: #aaffee;" rowspan="4">
	<p><a href="../working-sessions/#itg06:%20audubon%20core%20maintenance%20group%20annual%20meeting">ITG06 Audubon Core</a></p>
	<p>Primary: Steve Baskauf</p>
	<p><a href="https://youtu.be/O5A4IpIyn8w" target="_blank" title="ITG06 Audubon Core">Recorded Video</a></p>
</td>
<td style="background-color: #ffeeaa;" rowspan="4">
	<p><a href="../working-sessions/#ws02:%20abcd/dwc%20alignment%20working%20group">WS02: ABCD/DwC</a></p>
	<p>Primary: David Fichtmüller</p>
	<p>Support: Paula Zermoglio</p>
	<p><a href="https://youtu.be/aTWmsaVAVf0" target="_blank" title="WS02: ABCD/DwC">Recorded Video</a></p>
</td>
<td style="background-color: #aae5ff;" rowspan="4">
	<p><a href="../working-sessions/#itg10:%20task%20group%20on%20minimum%20information%20about%20a%20digital%20specimen%20(mids)">ITG10: MIDS</a></p>
	<p>Primary: Alex Hardisty</p>
	<p><a href="https://youtu.be/ZNdL7ttOKd8" target="_blank" title="ITG10: MIDS">Recorded Video</a></p>
</td>
<td style="background-color: #aabbff;" rowspan="4">
	<p><a href="../working-sessions/#itg04:%20best%20practices%20for%20the%20development%20of%20vocabularies%20of%20values%20(%22vocabularies%22)">ITG04: Vocabularies</a></p>
	<p>Primary: Paula Zermoglio</p>
	<p><a href="https://youtu.be/iAvaGpiO-g8" target="_blank" title="ITG04: Vocabularies">Recorded Video</a><p></p>
</td>
<td style="background-color: #e6ffaa;" rowspan="4">
	<p><a href="../working-sessions/#itg12:%20annotations%20interest%20group">ITG12: Annotations</a></p>
	<p>Primary: Paul J. Morris</p>
	<p>Support: James Macklin, Tim Robertson </p>
	<p><a href="https://youtu.be/FkYhs9lt1Ps" target="_blank" title="ITG12: Annotations">Recorded Video</a></p>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T12:30:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T13:00:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T13:30:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T14:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T14:30:00Z') );
  </script>
</td>
<td style="background-color: #aae5ff;" rowspan="3">
	<p><a href="../working-sessions/#itg03:%20collections%20descriptions%20task%20group">ITG03: Collection Descriptions (CD)</a></p>
	<p>Primary: Matt Woodburn</p>
	<p>Support: Deb Paul, Holly Little</p>
	<p><a href="https://youtu.be/L44dWAa-tF4" target="_blank" title="CD">Recorded Video</a></p>
</td>
<td style="background-color: #eeaaff;" rowspan="4">
	<p><a href="../working-sessions/#bof01:%20converging%20digital%20specimens%20and%20extended%20specimens%20-%20towards%20a%20global%20specification">BOF01: Global specification for specimens</a></p>
	<p>Primary: Alex Hardisty</p>
	<p>Support: Andrew Bentley</p>
	<p><a href="https://youtu.be/8ljokNRkjeo" target="_blank" title="Digital Specimens">Recorded Video</a></p>
</td>
<td style="background-color: #aaffee;" rowspan="4">
	<p><a href="../working-sessions/#itg02:%20darwin%20core%20maintenance%20group">ITG02: Darwin Core</a></p>
	<p>Primary: John Wieczorek</p>
	<p>Support: Paula Zermoglio, Tim Robertson</p>
	<p><a href="https://youtu.be/ooHOxGoCm18" target="_blank" title="DwC Maintenance">Recorded Video</a></p>
</td>
<td style="background-color: #ffeeaa;" rowspan="3">
	<p><a href="../working-sessions/#ws01:%20capturing%20ideas%20for%20the%20future%20of%20biocase%20provider%20software%20and%20the%20gbif%20integrated%20publishing%20toolkit%20(ipt)">WS01: BioCASe &amp; IPT; Part 1</a></p>
	<p>Primary: Jörg Holetschek</p>
	<p>Support: Tim Robertson</p>
	<p><a href="https://youtu.be/hU1I1ER9qLw" target="_blank" title="BioCASe/IPT">Recorded Video</a><p></p>
</td>
<td style="background-color: #ffeeaa;" rowspan="3">
	<p><a href="../working-sessions/#ws01:%20capturing%20ideas%20for%20the%20future%20of%20biocase%20provider%20software%20and%20the%20gbif%20integrated%20publishing%20toolkit%20(ipt)">WS01: BioCASe &amp; IPT; Part 2</a></p>
	<p>Primary: Jörg Holetschek</p>
	<p>Support: Tim Robertson</p>
	<p><a href="https://youtu.be/l4ORGpzHKe4" target="_blank" title="WS01: BioCASe+IPT(2)">Recorded Video</a></p>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T15:00:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T15:30:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T16:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T16:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T17:00:00Z') );
  </script>
</td>
<td style="background-color: #ffeeaa;" rowspan="3">
	<p><a href="../working-sessions/#intro:%20introduction%20to%20tdwg">INTRO: Introduction to TDWG</a></p>
	<p>Primary: Holly Little</p>
	<p>Support: Deb Paul</p>
	<p><a href="https://youtu.be/YC0N0fxwBxo" target="_blank" title="INTRO: Introduction to TDWG (2)">Recorded Video</a></p>
</td>
<td style="background-color: #e6ffaa;" rowspan="4">
	<p><a href="../working-sessions/#itg08:%20earth%20science%20and%20paleobiology%20interest%20group">ITG08: Earth Sci/Paleo (ESP)</a></p>
	<p>Primary: Denné Reed</p>
	<p>Support: Holly Little</p>
	<p><a href="https://youtu.be/q9r22lXlpIA" target="_blank" title="ITG08: Earth Sci/Paleo (ESP)">Recorded Video</a></p>
</td>
<td style="background-color: #bbffaa;" rowspan="4">
	<p><a href="../working-sessions/#itg11:%20species%20information%20interest%20group">ITG11: Species Info</a></p>
	<p>Primary: Paco Pando</p>
	<p><a href="https://youtu.be/lFi82CPmC2U" target="_blank" title="ITG11: Species Information">Recorded Video</a></p>
</td>
<td style="background-color: #aae5ff;" rowspan="4">
	<p><a href="../working-sessions/#ws03:%20living%20atlases%20workshop%20for%20end%20users">WS03: Living Atlases</a></p>
	<p>Primary: Marie-Elise Lecoq</p>
	<p>Support: Paula Zermoglio </p>
	<p><a href="https://youtu.be/LVR4weoOoRQ" target="_blank" title="WS03: Living Atlases">Recorded Video</a><p></p>
</td>
<td style="background-color: #aabbff;" rowspan="4">
	<p><a href="../working-sessions/#itg14:%20genomic%20biodiversity%20interest%20group">ITG14: Genomic Biodiversity</a></p>
	<p>Primary: Ramona Walls</p>
	<p><a href="https://youtu.be/FmrV6fQwyNQ" target="_blank" title="ITG14: Genomics">Recorded Video</a></p>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T17:30:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T18:00:00Z') );
  </script>
</td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T18:30:00Z') );
  </script>
</td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T19:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T19:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T20:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T20:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T21:00:00Z') );
  </script>
</td>
<td> </td>
<td style="background-color: #ffff99;" rowspan="4">
	<p><a href="../working-sessions/#itg01:%20taxon%20names%20and%20concepts">ITG01: TNC</a></p>
	<p>Primary: Niels Klazenga</p>
	<p>Support:</p>
	<p><a href="https://youtu.be/-bQLjUP0eRc" target="_blank" title="ITG01: TNC">Recorded Video</a></p>
</td>
<td> </td>
<td style="background-color: #e6ffaa;" rowspan="4">
	<p><a href="../working-sessions/#itg05:%20machine%20observations%20interest%20group">ITG05: Machine Observations</a></p>
	<p>Primary: Peggy Newman</p>
	<p>Support: Peter Desmet</p>
	<p><a href="https://youtu.be/dxoW-miXINo" target="_blank" title="ITG05: Machine Observations">Recorded Video</a></p>
</td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T21:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T22:00:00Z') );
  </script>
</td>
<td> </td>
<td style="background-color: #bbffaa;" rowspan="4">
	<p><a href="../working-sessions/#itg13:%20citizen%20science%20interest%20group">ITG13: Citizen Science</a></p>
	<p>Primary: Rob Stevenson</p>
	<p><a href="https://youtu.be/TxUf-krdhMw" target="_blank" title="ITG13: Citizen Science">Recorded Video</a></p>
</td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T22:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T23:00:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>
  <script type="text/javascript">
    document.write( horaLocal('2020-09-21T23:30:00Z') );
  </script>
</td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
</tbody>
</table>
