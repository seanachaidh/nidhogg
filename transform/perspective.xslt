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
							<xsl:when test="current()/@soort &eq; ik">
								<span><xsl:value-of select="current()" /></span>
							</xsl:when>
							<xsl:when test="current()/@soort &eq; hij">
								<span><xsl:value-of select="current()" /></span>
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
