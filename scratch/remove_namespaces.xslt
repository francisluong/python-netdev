<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="no"/>

    <!-- stylesheet to remove all namespaces from a document -->
    <!-- note: this will lead to attribute name clash, if an element contains two attributes with same local name but different namespace prefix -->
    <!-- nodes that cannot have a namespace are copied as such -->

    <!-- template to copy elements -->
    <xsl:template match="*">
        <xsl:element name="{local-name()}">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <!-- template to copy attributes -->
    <xsl:template match="@*">
        <xsl:attribute name="{local-name()}">
            <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>

    <!-- template to copy the rest of the nodes -->
    <xsl:template match="/|comment()|processing-instruction()|text()">
        <xsl:copy>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>
