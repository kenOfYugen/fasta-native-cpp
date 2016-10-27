{
	"targets": [
		{
			"includes": [
				"auto.gypi"
			],
			"sources": [
				"src/fasta.cc"
			],
			"clags_cc": [
				"-pipe",
				"-O3",
				"-fomit-frame-pointer",
				"-march=native",
				"-mfpmath=sse",
				"-msse3",
				"-std=c++11"
			],
			"link_settings":{
	      "ldflags": [
	        "-L/usr/lib -lpthread"
      	]
			}
		}
	],
	"includes": [
		"auto-top.gypi"
	]
}
