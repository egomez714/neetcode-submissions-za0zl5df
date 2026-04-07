class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0){
            return new ArrayList<>();
        }
        
        Map<String, List<String>> fMap = new HashMap<>();

        for(String str : strs){
            String fString = getFstring(str);

            if (fMap.containsKey(fString)){
                fMap.get(fString).add(str);
            }
            else{
                List<String> subList = new ArrayList<>();
                subList.add(str);
                fMap.put(fString,subList);
            }
        }
        return new ArrayList<>(fMap.values());
    }

    public String getFstring(String str){
        int [] freq = new int[26];
        for (char c : str.toCharArray()){
            freq[c-'a']++;
        }
        StringBuilder fString = new StringBuilder("");
        char c = 'a';
        for (int i : freq){
            fString.append(c);
            fString.append(i);
            c++;
        }
        return fString.toString();
    }
}
