from odetta.jobs.reference_counts_base import ReferenceCountsBase


class ReferenceCounts(ReferenceCountsBase):

    """
    TODO

    Look at ReferenceCountsBase, it defines most of the code shared by single/paired
    reference count jobs.
    """

    def mapper(self, key, pair):
        """
        TODO
        """
        x, y = pair

        # this assumes x and y have the same reference
        yield x['reference'], '-'.join(sorted([self.alignment_type(x), 
                                               self.alignment_type(y)]))


if __name__ == '__main__':
    ReferenceCounts.run()
