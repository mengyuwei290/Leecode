class Solution(object):
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            # 这个必须要交换保证前面数组相对较短
            m, n, A, B = n, m, B, A
        if n <= 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            # 要保证分割两段后，他们的长度相同(总长度为奇数时，前比后多1)
            i = (imin + imax) // 2
            j = (half_len - i)
            if i < m and B[j - 1] > A[i]:
                # i is too small
                imin = i + 1
            if i > 0 and A[i - 1] > B[j]:
                # i is too big
                imax = i - 1
            else:
                # max_left
                if i == 0:
                    max_left = B[j - 1]
                elif j == 0:
                    max_left = A[i - 1]
                else:
                    max_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return float(max_left)

                # max_right
                if i == m:
                    max_right = B[j]
                elif j == n:
                    max_right = A[i]
                else:
                    max_right = max(A[i], B[j])

                return max_left + max_right / 2.0


if __name__ == '__main__':
    ff = Solution()
    print(ff.findMedianSortedArrays([1, 3], [2]))
