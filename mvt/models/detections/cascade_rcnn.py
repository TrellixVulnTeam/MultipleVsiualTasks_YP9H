from ..model_builder import DETECTORS
from .base_detectors import TwoStageDetector


@DETECTORS.register_module()
class CascadeRCNN(TwoStageDetector):
    r"""Implementation of `Cascade R-CNN: Delving into High Quality Object
    Detection <https://arxiv.org/abs/1906.09756>`_"""

    def __init__(self, cfg):
        super(CascadeRCNN, self).__init__(cfg)

    def show_result(self, data, result, **kwargs):
        """Show prediction results of the detector."""
        if self.with_mask:
            ms_bbox_result, ms_segm_result = result
            if isinstance(ms_bbox_result, dict):
                result = (ms_bbox_result['ensemble'],
                          ms_segm_result['ensemble'])
        else:
            if isinstance(result, dict):
                result = result['ensemble']
        return super(CascadeRCNN, self).show_result(data, result, **kwargs)
