import os
import shutil
from download_file import download_file
from extractCRISPR import extractCRISPR
from find_consensus import find_consensus
from decide_leader import decide_leader
from findRelatedClusters import findRelatedClusters
from clusterModels import clusterModels
from performMSA_mview import performMSA_mview

def scenario_d_f_o(File, Archaea_Bacteria):	
	Archaea_Bacteria = Archaea_Bacteria.upper()	
	os.mkdir("temp_folder")			# create the temporary folder
	cmd = "chmod 777 temp_folder"	
	os.popen(cmd)					# Provide all the access permissions to the temporary folder using this statement
	Complete_partial_flag = download_file(File)
	if Complete_partial_flag == -1:
		return -1
	File = "temp_folder/" + File + ".fasta"		
	SequenceID = extractCRISPR(File,Complete_partial_flag,Archaea_Bacteria)
	
	if SequenceID == -1:
		return -1
	else:	
		find_consensus(SequenceID)
				
		decide_leader(File,Complete_partial_flag)   # find the leader of each reapeat
			
		ClustersOfEachRepeatArray = findRelatedClusters(Archaea_Bacteria, False) # find the related clusters that repeat belongs to
					
		clusterModels(Archaea_Bacteria, False, ClustersOfEachRepeatArray)   # find the final cluster of the repeat among the related clusters
			
		cmd = "chmod 777 Output/"   # provide all access permissions to all the files under 'Output' folder
		os.popen(cmd)
			
		if Complete_partial_flag == "COMPLETE": # if a genome is complete, then it is possible to visualize the multisequece alignment of the leader
			performMSA_mview(SequenceID,False)  # with the cluster family members
