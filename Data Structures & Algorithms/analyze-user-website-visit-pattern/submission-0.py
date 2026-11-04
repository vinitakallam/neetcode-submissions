class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = defaultdict(list)

        for time, user, site in sorted(zip(timestamp, username, website)):
            visits[user].append(site)

        counts = Counter()
        for sites in visits.values():
            unique_patterns = set(combinations(sites, 3))
            counts.update(unique_patterns)

        best = None

        for pattern in counts:
            if best == None:
                best = pattern
            elif counts[best] < counts[pattern]:
                best = pattern
            elif counts[best] == counts[pattern] and pattern < best:
                best = pattern

        return list(best) 