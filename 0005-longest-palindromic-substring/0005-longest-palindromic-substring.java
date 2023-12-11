class Solution {
    public String longestPalindrome(String s) {
        Map<Integer,String> mapEven =new HashMap();
        Map<Integer,String> mapOdd =new HashMap();
        String longestPalyndrom="";
        int n=s.length();
        Map<Integer,String> tmp_map_Even =new HashMap();
        Map<Integer,String> tmp_map_Odd =new HashMap();

//      initializing the maps and longestPalindrome
        for(int i=0;i<n-1;i++){
            mapOdd.put(i,s.substring(i,i+1));
            if(s.substring(i,i+1).equals(s.substring(i+1,i+2)))
                mapEven.put(i,s.substring(i,i+2));
        }
        mapOdd.put(n-1,s.substring(n-1,n));
        if(mapEven.size()!=0)
            longestPalyndrom=mapEven.get(0);
        else if (mapOdd.size()!=0)
            longestPalyndrom=mapOdd.get(0);

 //     *********************************

        for(int i=1;i<=n/2;i++){
            // loop through the mapEven
            tmp_map_Even = (Map<Integer,String>) Map.copyOf(mapEven);
            for(int j : tmp_map_Even.keySet() ){
                if(j-i < 0 || j+i+1 > n-1){
                    mapEven.remove(j);
                    continue;
                }
                if(s.substring(j-i,j-i+1).equals(s.substring(j+i+1,j+i+2)))
                    mapEven.put(j,s.substring(j-i,j-i+1)+mapEven.get(j)+s.substring(j+i+1,j+i+2));
                else mapEven.remove(j);
            }

            // loop through the mapOdd
            tmp_map_Odd = (Map<Integer,String>) Map.copyOf(mapOdd);
            for(int j : tmp_map_Odd.keySet() ){
                if(j-i < 0 || j+i > n-1){
                    mapOdd.remove(j);
                    continue;
                }  
                if(s.substring(j-i,j-i+1).equals(s.substring(j+i,j+i+1)))
                    mapOdd.put(j,s.substring(j-i,j-i+1)+mapOdd.get(j)+s.substring(j+i,j+i+1));
                else  mapOdd.remove(j);
            }

            if(mapEven.size()!=0)
                longestPalyndrom=mapEven.get(mapEven.keySet().toArray()[0]);
            else if (mapOdd.size()!=0)
                longestPalyndrom=mapOdd.get(mapOdd.keySet().toArray()[0]);
            else if(tmp_map_Even.size()!=0)
                longestPalyndrom=tmp_map_Even.get(tmp_map_Even.keySet().toArray()[0]);
            else if(tmp_map_Odd.size()!=0)
                longestPalyndrom=tmp_map_Odd.get(tmp_map_Odd.keySet().toArray()[0]);
            else {System.out.println("the maps are emplty"); return longestPalyndrom;}

        }
        return longestPalyndrom;

    }
}