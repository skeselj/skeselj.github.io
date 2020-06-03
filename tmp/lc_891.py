from typing import Dict


class Solution:
    _powers_of_two = {}

    def twoToThe(self, k: int) -> int:
        if k in self._powers_of_two:
            return self._powers_of_two[k]
        if k == 1:
            return 2
        else:
            output = 2 ** k
            self._powers_of_two[k] = output
            return output

    def sumSubseqWidths(self, A: List[int]) -> int:
        element_to_count = {}
        for idx, element in enumerate(A):
            if element not in element_to_count:
                element_to_count[element] = 0
            element_to_count[element] += 1

        sorted_elements = sorted(list(element_to_count.keys()))

        output = 0

        for min_idx in range(len(sorted_elements) - 1):
            min_el = sorted_elements[min_idx]

            min_el_count = element_to_count[min_el]
            num_ways_to_include_min_el = self.twoToThe(min_el_count) - 1

            curr_subseq_count = num_ways_to_include_min_el

            for max_idx in range(min_idx + 1, len(sorted_elements)):
                max_el = sorted_elements[max_idx]

                max_el_count = element_to_count[max_el]
                num_ways_to_include_max_el = self.twoToThe(max_el_count) - 1

                output += (curr_subseq_count * num_ways_to_include_max_el) * (max_el - min_el)

                curr_subseq_count *= (num_ways_to_include_max_el + 1)

        return output % 1000000007