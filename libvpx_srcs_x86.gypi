# This file is generated. Do not edit.
# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'sources': [
    '<(libvpx_source)/vp8/common/alloccommon.c',
    '<(libvpx_source)/vp8/common/alloccommon.h',
    '<(libvpx_source)/vp8/common/blockd.c',
    '<(libvpx_source)/vp8/common/blockd.h',
    '<(libvpx_source)/vp8/common/coefupdateprobs.h',
    '<(libvpx_source)/vp8/common/common.h',
    '<(libvpx_source)/vp8/common/debugmodes.c',
    '<(libvpx_source)/vp8/common/default_coef_probs.h',
    '<(libvpx_source)/vp8/common/dequantize.c',
    '<(libvpx_source)/vp8/common/entropy.c',
    '<(libvpx_source)/vp8/common/entropy.h',
    '<(libvpx_source)/vp8/common/entropymode.c',
    '<(libvpx_source)/vp8/common/entropymode.h',
    '<(libvpx_source)/vp8/common/entropymv.c',
    '<(libvpx_source)/vp8/common/entropymv.h',
    '<(libvpx_source)/vp8/common/extend.c',
    '<(libvpx_source)/vp8/common/extend.h',
    '<(libvpx_source)/vp8/common/filter.c',
    '<(libvpx_source)/vp8/common/filter.h',
    '<(libvpx_source)/vp8/common/findnearmv.c',
    '<(libvpx_source)/vp8/common/findnearmv.h',
    '<(libvpx_source)/vp8/common/generic/systemdependent.c',
    '<(libvpx_source)/vp8/common/header.h',
    '<(libvpx_source)/vp8/common/idct_blk.c',
    '<(libvpx_source)/vp8/common/idctllm.c',
    '<(libvpx_source)/vp8/common/invtrans.h',
    '<(libvpx_source)/vp8/common/loopfilter.c',
    '<(libvpx_source)/vp8/common/loopfilter.h',
    '<(libvpx_source)/vp8/common/loopfilter_filters.c',
    '<(libvpx_source)/vp8/common/mbpitch.c',
    '<(libvpx_source)/vp8/common/mfqe.c',
    '<(libvpx_source)/vp8/common/modecont.c',
    '<(libvpx_source)/vp8/common/modecont.h',
    '<(libvpx_source)/vp8/common/mv.h',
    '<(libvpx_source)/vp8/common/onyx.h',
    '<(libvpx_source)/vp8/common/onyxc_int.h',
    '<(libvpx_source)/vp8/common/onyxd.h',
    '<(libvpx_source)/vp8/common/postproc.c',
    '<(libvpx_source)/vp8/common/postproc.h',
    '<(libvpx_source)/vp8/common/ppflags.h',
    '<(libvpx_source)/vp8/common/quant_common.c',
    '<(libvpx_source)/vp8/common/quant_common.h',
    '<(libvpx_source)/vp8/common/reconinter.c',
    '<(libvpx_source)/vp8/common/reconinter.h',
    '<(libvpx_source)/vp8/common/reconintra.c',
    '<(libvpx_source)/vp8/common/reconintra4x4.c',
    '<(libvpx_source)/vp8/common/reconintra4x4.h',
    '<(libvpx_source)/vp8/common/rtcd.c',
    '<(libvpx_source)/vp8/common/sad_c.c',
    '<(libvpx_source)/vp8/common/setupintrarecon.c',
    '<(libvpx_source)/vp8/common/setupintrarecon.h',
    '<(libvpx_source)/vp8/common/swapyv12buffer.c',
    '<(libvpx_source)/vp8/common/swapyv12buffer.h',
    '<(libvpx_source)/vp8/common/systemdependent.h',
    '<(libvpx_source)/vp8/common/threading.h',
    '<(libvpx_source)/vp8/common/treecoder.c',
    '<(libvpx_source)/vp8/common/treecoder.h',
    '<(libvpx_source)/vp8/common/variance.h',
    '<(libvpx_source)/vp8/common/variance_c.c',
    '<(libvpx_source)/vp8/common/vp8_entropymodedata.h',
    '<(libvpx_source)/vp8/common/x86/dequantize_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/filter_x86.c',
    '<(libvpx_source)/vp8/common/x86/filter_x86.h',
    '<(libvpx_source)/vp8/common/x86/idctllm_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/idctllm_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/iwalsh_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/iwalsh_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/loopfilter_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/loopfilter_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/loopfilter_x86.c',
    '<(libvpx_source)/vp8/common/x86/mfqe_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/postproc_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/postproc_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/recon_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/recon_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/sad_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/sad_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/sad_sse3.asm',
    '<(libvpx_source)/vp8/common/x86/sad_sse4.asm',
    '<(libvpx_source)/vp8/common/x86/sad_ssse3.asm',
    '<(libvpx_source)/vp8/common/x86/subpixel_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/subpixel_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/subpixel_ssse3.asm',
    '<(libvpx_source)/vp8/common/x86/variance_impl_mmx.asm',
    '<(libvpx_source)/vp8/common/x86/variance_impl_sse2.asm',
    '<(libvpx_source)/vp8/common/x86/variance_impl_ssse3.asm',
    '<(libvpx_source)/vp8/common/x86/vp8_asm_stubs.c',
    '<(libvpx_source)/vp8/decoder/dboolhuff.c',
    '<(libvpx_source)/vp8/decoder/dboolhuff.h',
    '<(libvpx_source)/vp8/decoder/decodeframe.c',
    '<(libvpx_source)/vp8/decoder/decodemv.c',
    '<(libvpx_source)/vp8/decoder/decodemv.h',
    '<(libvpx_source)/vp8/decoder/decoderthreading.h',
    '<(libvpx_source)/vp8/decoder/detokenize.c',
    '<(libvpx_source)/vp8/decoder/detokenize.h',
    '<(libvpx_source)/vp8/decoder/onyxd_if.c',
    '<(libvpx_source)/vp8/decoder/onyxd_int.h',
    '<(libvpx_source)/vp8/decoder/threading.c',
    '<(libvpx_source)/vp8/decoder/treereader.h',
    '<(libvpx_source)/vp8/encoder/bitstream.c',
    '<(libvpx_source)/vp8/encoder/bitstream.h',
    '<(libvpx_source)/vp8/encoder/block.h',
    '<(libvpx_source)/vp8/encoder/boolhuff.c',
    '<(libvpx_source)/vp8/encoder/boolhuff.h',
    '<(libvpx_source)/vp8/encoder/dct.c',
    '<(libvpx_source)/vp8/encoder/dct_value_cost.h',
    '<(libvpx_source)/vp8/encoder/dct_value_tokens.h',
    '<(libvpx_source)/vp8/encoder/defaultcoefcounts.h',
    '<(libvpx_source)/vp8/encoder/denoising.c',
    '<(libvpx_source)/vp8/encoder/denoising.h',
    '<(libvpx_source)/vp8/encoder/encodeframe.c',
    '<(libvpx_source)/vp8/encoder/encodeframe.h',
    '<(libvpx_source)/vp8/encoder/encodeintra.c',
    '<(libvpx_source)/vp8/encoder/encodeintra.h',
    '<(libvpx_source)/vp8/encoder/encodemb.c',
    '<(libvpx_source)/vp8/encoder/encodemb.h',
    '<(libvpx_source)/vp8/encoder/encodemv.c',
    '<(libvpx_source)/vp8/encoder/encodemv.h',
    '<(libvpx_source)/vp8/encoder/ethreading.c',
    '<(libvpx_source)/vp8/encoder/firstpass.h',
    '<(libvpx_source)/vp8/encoder/lookahead.c',
    '<(libvpx_source)/vp8/encoder/lookahead.h',
    '<(libvpx_source)/vp8/encoder/mcomp.c',
    '<(libvpx_source)/vp8/encoder/mcomp.h',
    '<(libvpx_source)/vp8/encoder/modecosts.c',
    '<(libvpx_source)/vp8/encoder/modecosts.h',
    '<(libvpx_source)/vp8/encoder/mr_dissim.c',
    '<(libvpx_source)/vp8/encoder/mr_dissim.h',
    '<(libvpx_source)/vp8/encoder/onyx_if.c',
    '<(libvpx_source)/vp8/encoder/onyx_int.h',
    '<(libvpx_source)/vp8/encoder/pickinter.c',
    '<(libvpx_source)/vp8/encoder/pickinter.h',
    '<(libvpx_source)/vp8/encoder/picklpf.c',
    '<(libvpx_source)/vp8/encoder/quantize.c',
    '<(libvpx_source)/vp8/encoder/quantize.h',
    '<(libvpx_source)/vp8/encoder/ratectrl.c',
    '<(libvpx_source)/vp8/encoder/ratectrl.h',
    '<(libvpx_source)/vp8/encoder/rdopt.c',
    '<(libvpx_source)/vp8/encoder/rdopt.h',
    '<(libvpx_source)/vp8/encoder/segmentation.c',
    '<(libvpx_source)/vp8/encoder/segmentation.h',
    '<(libvpx_source)/vp8/encoder/tokenize.c',
    '<(libvpx_source)/vp8/encoder/tokenize.h',
    '<(libvpx_source)/vp8/encoder/treewriter.c',
    '<(libvpx_source)/vp8/encoder/treewriter.h',
    '<(libvpx_source)/vp8/encoder/x86/dct_mmx.asm',
    '<(libvpx_source)/vp8/encoder/x86/dct_sse2.asm',
    '<(libvpx_source)/vp8/encoder/x86/encodeopt.asm',
    '<(libvpx_source)/vp8/encoder/x86/fwalsh_sse2.asm',
    '<(libvpx_source)/vp8/encoder/x86/quantize_mmx.asm',
    '<(libvpx_source)/vp8/encoder/x86/subtract_mmx.asm',
    '<(libvpx_source)/vp8/encoder/x86/subtract_sse2.asm',
    '<(libvpx_source)/vp8/vp8_cx_iface.c',
    '<(libvpx_source)/vp8/vp8_dx_iface.c',
    '<(libvpx_source)/vp9/common/vp9_alloccommon.c',
    '<(libvpx_source)/vp9/common/vp9_alloccommon.h',
    '<(libvpx_source)/vp9/common/vp9_blockd.c',
    '<(libvpx_source)/vp9/common/vp9_blockd.h',
    '<(libvpx_source)/vp9/common/vp9_common.h',
    '<(libvpx_source)/vp9/common/vp9_common_data.c',
    '<(libvpx_source)/vp9/common/vp9_common_data.h',
    '<(libvpx_source)/vp9/common/vp9_convolve.c',
    '<(libvpx_source)/vp9/common/vp9_convolve.h',
    '<(libvpx_source)/vp9/common/vp9_debugmodes.c',
    '<(libvpx_source)/vp9/common/vp9_entropy.c',
    '<(libvpx_source)/vp9/common/vp9_entropy.h',
    '<(libvpx_source)/vp9/common/vp9_entropymode.c',
    '<(libvpx_source)/vp9/common/vp9_entropymode.h',
    '<(libvpx_source)/vp9/common/vp9_entropymv.c',
    '<(libvpx_source)/vp9/common/vp9_entropymv.h',
    '<(libvpx_source)/vp9/common/vp9_enums.h',
    '<(libvpx_source)/vp9/common/vp9_filter.c',
    '<(libvpx_source)/vp9/common/vp9_filter.h',
    '<(libvpx_source)/vp9/common/vp9_frame_buffers.c',
    '<(libvpx_source)/vp9/common/vp9_frame_buffers.h',
    '<(libvpx_source)/vp9/common/vp9_idct.c',
    '<(libvpx_source)/vp9/common/vp9_idct.h',
    '<(libvpx_source)/vp9/common/vp9_loopfilter.c',
    '<(libvpx_source)/vp9/common/vp9_loopfilter.h',
    '<(libvpx_source)/vp9/common/vp9_loopfilter_filters.c',
    '<(libvpx_source)/vp9/common/vp9_mv.h',
    '<(libvpx_source)/vp9/common/vp9_mvref_common.c',
    '<(libvpx_source)/vp9/common/vp9_mvref_common.h',
    '<(libvpx_source)/vp9/common/vp9_onyxc_int.h',
    '<(libvpx_source)/vp9/common/vp9_ppflags.h',
    '<(libvpx_source)/vp9/common/vp9_pred_common.c',
    '<(libvpx_source)/vp9/common/vp9_pred_common.h',
    '<(libvpx_source)/vp9/common/vp9_prob.c',
    '<(libvpx_source)/vp9/common/vp9_prob.h',
    '<(libvpx_source)/vp9/common/vp9_quant_common.c',
    '<(libvpx_source)/vp9/common/vp9_quant_common.h',
    '<(libvpx_source)/vp9/common/vp9_reconinter.c',
    '<(libvpx_source)/vp9/common/vp9_reconinter.h',
    '<(libvpx_source)/vp9/common/vp9_reconintra.c',
    '<(libvpx_source)/vp9/common/vp9_reconintra.h',
    '<(libvpx_source)/vp9/common/vp9_rtcd.c',
    '<(libvpx_source)/vp9/common/vp9_scale.c',
    '<(libvpx_source)/vp9/common/vp9_scale.h',
    '<(libvpx_source)/vp9/common/vp9_scan.c',
    '<(libvpx_source)/vp9/common/vp9_scan.h',
    '<(libvpx_source)/vp9/common/vp9_seg_common.c',
    '<(libvpx_source)/vp9/common/vp9_seg_common.h',
    '<(libvpx_source)/vp9/common/vp9_systemdependent.h',
    '<(libvpx_source)/vp9/common/vp9_textblit.h',
    '<(libvpx_source)/vp9/common/vp9_thread.c',
    '<(libvpx_source)/vp9/common/vp9_thread.h',
    '<(libvpx_source)/vp9/common/vp9_tile_common.c',
    '<(libvpx_source)/vp9/common/vp9_tile_common.h',
    '<(libvpx_source)/vp9/common/x86/vp9_asm_stubs.c',
    '<(libvpx_source)/vp9/common/x86/vp9_copy_sse2.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_idct_intrin_sse2.h',
    '<(libvpx_source)/vp9/common/x86/vp9_intrapred_sse2.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_intrapred_ssse3.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_loopfilter_mmx.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_subpixel_8t_sse2.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_subpixel_8t_ssse3.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_subpixel_bilinear_sse2.asm',
    '<(libvpx_source)/vp9/common/x86/vp9_subpixel_bilinear_ssse3.asm',
    '<(libvpx_source)/vp9/decoder/vp9_decodeframe.c',
    '<(libvpx_source)/vp9/decoder/vp9_decodeframe.h',
    '<(libvpx_source)/vp9/decoder/vp9_decodemv.c',
    '<(libvpx_source)/vp9/decoder/vp9_decodemv.h',
    '<(libvpx_source)/vp9/decoder/vp9_decoder.c',
    '<(libvpx_source)/vp9/decoder/vp9_decoder.h',
    '<(libvpx_source)/vp9/decoder/vp9_detokenize.c',
    '<(libvpx_source)/vp9/decoder/vp9_detokenize.h',
    '<(libvpx_source)/vp9/decoder/vp9_dsubexp.c',
    '<(libvpx_source)/vp9/decoder/vp9_dsubexp.h',
    '<(libvpx_source)/vp9/decoder/vp9_dthread.c',
    '<(libvpx_source)/vp9/decoder/vp9_dthread.h',
    '<(libvpx_source)/vp9/decoder/vp9_read_bit_buffer.c',
    '<(libvpx_source)/vp9/decoder/vp9_read_bit_buffer.h',
    '<(libvpx_source)/vp9/decoder/vp9_reader.c',
    '<(libvpx_source)/vp9/decoder/vp9_reader.h',
    '<(libvpx_source)/vp9/encoder/vp9_aq_complexity.c',
    '<(libvpx_source)/vp9/encoder/vp9_aq_complexity.h',
    '<(libvpx_source)/vp9/encoder/vp9_aq_cyclicrefresh.c',
    '<(libvpx_source)/vp9/encoder/vp9_aq_cyclicrefresh.h',
    '<(libvpx_source)/vp9/encoder/vp9_aq_variance.c',
    '<(libvpx_source)/vp9/encoder/vp9_aq_variance.h',
    '<(libvpx_source)/vp9/encoder/vp9_bitstream.c',
    '<(libvpx_source)/vp9/encoder/vp9_bitstream.h',
    '<(libvpx_source)/vp9/encoder/vp9_block.h',
    '<(libvpx_source)/vp9/encoder/vp9_context_tree.c',
    '<(libvpx_source)/vp9/encoder/vp9_context_tree.h',
    '<(libvpx_source)/vp9/encoder/vp9_cost.c',
    '<(libvpx_source)/vp9/encoder/vp9_cost.h',
    '<(libvpx_source)/vp9/encoder/vp9_dct.c',
    '<(libvpx_source)/vp9/encoder/vp9_encodeframe.c',
    '<(libvpx_source)/vp9/encoder/vp9_encodeframe.h',
    '<(libvpx_source)/vp9/encoder/vp9_encodemb.c',
    '<(libvpx_source)/vp9/encoder/vp9_encodemb.h',
    '<(libvpx_source)/vp9/encoder/vp9_encodemv.c',
    '<(libvpx_source)/vp9/encoder/vp9_encodemv.h',
    '<(libvpx_source)/vp9/encoder/vp9_encoder.c',
    '<(libvpx_source)/vp9/encoder/vp9_encoder.h',
    '<(libvpx_source)/vp9/encoder/vp9_extend.c',
    '<(libvpx_source)/vp9/encoder/vp9_extend.h',
    '<(libvpx_source)/vp9/encoder/vp9_firstpass.c',
    '<(libvpx_source)/vp9/encoder/vp9_firstpass.h',
    '<(libvpx_source)/vp9/encoder/vp9_lookahead.c',
    '<(libvpx_source)/vp9/encoder/vp9_lookahead.h',
    '<(libvpx_source)/vp9/encoder/vp9_mbgraph.c',
    '<(libvpx_source)/vp9/encoder/vp9_mbgraph.h',
    '<(libvpx_source)/vp9/encoder/vp9_mcomp.c',
    '<(libvpx_source)/vp9/encoder/vp9_mcomp.h',
    '<(libvpx_source)/vp9/encoder/vp9_picklpf.c',
    '<(libvpx_source)/vp9/encoder/vp9_picklpf.h',
    '<(libvpx_source)/vp9/encoder/vp9_pickmode.c',
    '<(libvpx_source)/vp9/encoder/vp9_pickmode.h',
    '<(libvpx_source)/vp9/encoder/vp9_quantize.c',
    '<(libvpx_source)/vp9/encoder/vp9_quantize.h',
    '<(libvpx_source)/vp9/encoder/vp9_ratectrl.c',
    '<(libvpx_source)/vp9/encoder/vp9_ratectrl.h',
    '<(libvpx_source)/vp9/encoder/vp9_rd.c',
    '<(libvpx_source)/vp9/encoder/vp9_rd.h',
    '<(libvpx_source)/vp9/encoder/vp9_rdopt.c',
    '<(libvpx_source)/vp9/encoder/vp9_rdopt.h',
    '<(libvpx_source)/vp9/encoder/vp9_resize.c',
    '<(libvpx_source)/vp9/encoder/vp9_resize.h',
    '<(libvpx_source)/vp9/encoder/vp9_sad.c',
    '<(libvpx_source)/vp9/encoder/vp9_segmentation.c',
    '<(libvpx_source)/vp9/encoder/vp9_segmentation.h',
    '<(libvpx_source)/vp9/encoder/vp9_speed_features.c',
    '<(libvpx_source)/vp9/encoder/vp9_speed_features.h',
    '<(libvpx_source)/vp9/encoder/vp9_subexp.c',
    '<(libvpx_source)/vp9/encoder/vp9_subexp.h',
    '<(libvpx_source)/vp9/encoder/vp9_svc_layercontext.c',
    '<(libvpx_source)/vp9/encoder/vp9_svc_layercontext.h',
    '<(libvpx_source)/vp9/encoder/vp9_temporal_filter.c',
    '<(libvpx_source)/vp9/encoder/vp9_temporal_filter.h',
    '<(libvpx_source)/vp9/encoder/vp9_tokenize.c',
    '<(libvpx_source)/vp9/encoder/vp9_tokenize.h',
    '<(libvpx_source)/vp9/encoder/vp9_treewriter.c',
    '<(libvpx_source)/vp9/encoder/vp9_treewriter.h',
    '<(libvpx_source)/vp9/encoder/vp9_variance.c',
    '<(libvpx_source)/vp9/encoder/vp9_variance.h',
    '<(libvpx_source)/vp9/encoder/vp9_write_bit_buffer.c',
    '<(libvpx_source)/vp9/encoder/vp9_write_bit_buffer.h',
    '<(libvpx_source)/vp9/encoder/vp9_writer.c',
    '<(libvpx_source)/vp9/encoder/vp9_writer.h',
    '<(libvpx_source)/vp9/encoder/x86/vp9_dct_mmx.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_error_sse2.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_sad4d_sse2.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_sad_mmx.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_sad_sse2.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_sad_sse3.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_sad_sse4.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_sad_ssse3.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_subpel_variance.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_subtract_sse2.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_temporal_filter_apply_sse2.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_variance_impl_mmx.asm',
    '<(libvpx_source)/vp9/encoder/x86/vp9_variance_impl_sse2.asm',
    '<(libvpx_source)/vp9/vp9_cx_iface.c',
    '<(libvpx_source)/vp9/vp9_dx_iface.c',
    '<(libvpx_source)/vp9/vp9_iface_common.h',
    '<(libvpx_source)/vpx/internal/vpx_codec_internal.h',
    '<(libvpx_source)/vpx/internal/vpx_psnr.h',
    '<(libvpx_source)/vpx/src/vpx_codec.c',
    '<(libvpx_source)/vpx/src/vpx_decoder.c',
    '<(libvpx_source)/vpx/src/vpx_encoder.c',
    '<(libvpx_source)/vpx/src/vpx_image.c',
    '<(libvpx_source)/vpx/src/vpx_psnr.c',
    '<(libvpx_source)/vpx/vp8.h',
    '<(libvpx_source)/vpx/vp8cx.h',
    '<(libvpx_source)/vpx/vp8dx.h',
    '<(libvpx_source)/vpx/vpx_codec.h',
    '<(libvpx_source)/vpx/vpx_decoder.h',
    '<(libvpx_source)/vpx/vpx_encoder.h',
    '<(libvpx_source)/vpx/vpx_frame_buffer.h',
    '<(libvpx_source)/vpx/vpx_image.h',
    '<(libvpx_source)/vpx/vpx_integer.h',
    '<(libvpx_source)/vpx_mem/include/vpx_mem_intrnl.h',
    '<(libvpx_source)/vpx_mem/vpx_mem.c',
    '<(libvpx_source)/vpx_mem/vpx_mem.h',
    '<(libvpx_source)/vpx_ports/asm_offsets.h',
    '<(libvpx_source)/vpx_ports/emmintrin_compat.h',
    '<(libvpx_source)/vpx_ports/emms.asm',
    '<(libvpx_source)/vpx_ports/mem.h',
    '<(libvpx_source)/vpx_ports/mem_ops.h',
    '<(libvpx_source)/vpx_ports/mem_ops_aligned.h',
    '<(libvpx_source)/vpx_ports/vpx_once.h',
    '<(libvpx_source)/vpx_ports/vpx_timer.h',
    '<(libvpx_source)/vpx_ports/x86.h',
    '<(libvpx_source)/vpx_ports/x86_abi_support.asm',
    '<(libvpx_source)/vpx_scale/generic/gen_scalers.c',
    '<(libvpx_source)/vpx_scale/generic/vpx_scale.c',
    '<(libvpx_source)/vpx_scale/generic/yv12config.c',
    '<(libvpx_source)/vpx_scale/generic/yv12extend.c',
    '<(libvpx_source)/vpx_scale/vpx_scale.h',
    '<(libvpx_source)/vpx_scale/vpx_scale_rtcd.c',
    '<(libvpx_source)/vpx_scale/yv12config.h',
  ],
}
