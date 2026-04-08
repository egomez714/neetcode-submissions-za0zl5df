class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordTracker = new HashMap<>();

        for (int i = 0; i < strs.length; i++){
            int[] wordFreq = new int[26];
            for (int j = 0; j < strs[i].length(); j++){
                wordFreq[strs[i].charAt(j) - 'a']++;
            }
            String index = Arrays.toString(wordFreq);

            wordTracker.putIfAbsent(index, new ArrayList<>());
            wordTracker.get(index).add(strs[i]);
        }
        return new ArrayList<List<String>>(wordTracker.values());
    }
}
