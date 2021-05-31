

rule format_name:
    input:
        "BAM_FILES/DENISOV_DENISOV_ADNA.bam"
    output:
        "BAM_FILES/DENISOV_DENISOV_ADNA_FRMT.bam"
    shell:
        "bwa mem {input} | samtools view -Sb - > {output}"
		"samtools view -H {input} | sed -e 's/SN:\([0-9XY]\)/SN:chr\1/' -e 's/SN:MT/SN:chrM/' | samtools reheader - {input} > {output};"