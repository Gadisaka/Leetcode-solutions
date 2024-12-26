def longestones(nums , k):
        max_w = 0
        zero_count = 0
        l = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            
            w = r - l + 1
            max_w = max(max_w , w)

        return max_w





