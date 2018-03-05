<?xml version="1.0"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<html>
			<body>
				<h2>Zinnen voor bestand <div class="info"><xsl:value-of select="nidhoggfile/@info" /></div></h2>
				<div class="bookcontent">
					<xsl:for-each select="nidhoggfile/zin">
						<xsl:choose>
							<xsl:when test="current()/@soort &#61; ik">
								<span class="ik"><xsl:value-of select="current()" /></span>
							</xsl:when>
							<xsl:when test="current()/@soort &#61; hij">
								<span class="hij"><xsl:value-of select="current()" /></span>
							</xsl:when>
							<xsl:otherwise>
								<span><xsl:value-of select="current()" /></span>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:for-each>
				</div>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>
