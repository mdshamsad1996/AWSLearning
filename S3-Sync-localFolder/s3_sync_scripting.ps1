$base_path = 'E:\MyLearning\aws\S3-Sync-localFolder\my_data\'
$customers = 'A','B','C','D' 
$year = 2019
$month =  'Jan'
for($i = 0;$i -le ($customers.length-1); $i +=1){
	$sync_path = $base_path+'\customer_'+$customers[$i]+'\'+$year+'\'+$month
	$s3_Sync_path = 'customer_'+$customers[$i]+'/'+$year+'/'+$month
	aws s3 sync $sync_path s3://my-sync-bucket-1996/$s3_Sync_path
}