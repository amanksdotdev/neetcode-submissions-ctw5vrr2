class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const store = new Map();
        const startingCharCode = 'a'.charCodeAt(0);
        for (let s of strs) {
            const alphaArray = new Array(26).fill(0);
            for (let c of s) {
                let idx = c.charCodeAt(0) - startingCharCode;
                alphaArray[idx]++;
            }
            const key = alphaArray.toString();
            if(store.has(key)) {
                store.get(key).push(s)
            } else {
                store.set(key, [s]);
            }
        }
        console.log(store)
        return Array.from(store.values());
    }
}
