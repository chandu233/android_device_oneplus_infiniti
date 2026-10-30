#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils:../../../hardware/oplus/extract-utils-ext python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils_oplus import (
    add_generated_thermal_engine_config,
)

namespace_imports = [
    'hardware/oplus',
    'hardware/qcom-caf/sm8850',
    'vendor/oneplus/sm8850-common',
    'vendor/qcom/opensource/commonsys-intf/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libhcsutils',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'odm/etc/camera/CameraHWConfiguration.config': blob_fixup()
        # Disable face detection AE behaviour
        .regex_replace(r'(enableSWfdForThirdCamUnit += )TRUE', r'\1FALSE')
        .regex_replace(r'(fdSupport += )TRUE;', r'\1FALSE;'),
    'odm/etc/init/init.camera_process.rc': blob_fixup()
        .regex_replace('    delete_recursion', '    #delete_recursion'),
    (
        'odm/etc/libnfc-mtp-SN220.conf_24831',
        'odm/etc/libnfc-mtp-SN220.conf_24863',
    ): blob_fixup()
        .regex_replace('(NXPLOG_.*_LOGLEVEL)=0x03', '\\1=0x02')
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    (
        'odm/lib64/camera/com.qti.sensor.infinitifront.so',
        'odm/lib64/camera/com.qti.sensor.infinitimain.so',
        'odm/lib64/camera/com.qti.sensor.infinititele.so',
        'odm/lib64/camera/com.qti.sensor.infinitiultrawide.so',
        'odm/lib64/camera/components/com.oplus.node.mvgsat.so',
        'odm/lib64/com.oplus.mcx.linearmapper.so',
        'odm/lib64/libextensionlayer.so',
        'vendor/lib64/camera/components/com.qti.eisv2.so',
        'vendor/lib64/camera/components/com.qti.hwcfg.ipe.so',
        'vendor/lib64/camera/components/com.qti.node.aon.so',
        'vendor/lib64/camera/components/com.qti.node.depth.so',
        'vendor/lib64/camera/components/com.qti.node.depthprovider.so',
        'vendor/lib64/camera/components/com.qti.node.eisv2.so',
        'vendor/lib64/camera/components/com.qti.node.eisv3.so',
        'vendor/lib64/camera/components/com.qti.node.evadepth.so',
        'vendor/lib64/camera/components/com.qti.node.evaitof.so',
        'vendor/lib64/camera/components/com.qti.node.evawarp.so',
        'vendor/lib64/camera/components/com.qti.node.frc.so',
        'vendor/lib64/camera/components/com.qti.node.gme.so',
        'vendor/lib64/camera/components/com.qti.node.gyrornn.so',
        'vendor/lib64/camera/components/com.qti.node.hdr10pgen.so',
        'vendor/lib64/camera/components/com.qti.node.hdr10phist.so',
        'vendor/lib64/camera/components/com.qti.node.hdralign.so',
        'vendor/lib64/camera/components/com.qti.node.itofpreprocess.so',
        'vendor/lib64/camera/components/com.qti.node.mctfalign.so',
        'vendor/lib64/camera/components/com.qti.node.ml.so',
        'vendor/lib64/camera/components/com.qti.node.mlinference.so',
        'vendor/lib64/camera/components/com.qti.node.mmfalign.so',
        'vendor/lib64/camera/components/com.qti.node.multiport.so',
        'vendor/lib64/camera/components/com.qti.node.muxer.so',
        'vendor/lib64/camera/components/com.qti.node.qsatalign.so',
        'vendor/lib64/camera/components/com.qti.node.rectification.so',
        'vendor/lib64/camera/components/com.qti.node.sat.so',
        'vendor/lib64/camera/components/com.qti.node.seg.so',
        'vendor/lib64/camera/components/com.qti.node.spdepth.so',
        'vendor/lib64/camera/components/com.qti.node.swaidenoiser.so',
        'vendor/lib64/camera/components/com.qti.node.swbestats.so',
        'vendor/lib64/camera/components/com.qti.node.swec.so',
        'vendor/lib64/camera/components/com.qti.node.swfusion.so',
        'vendor/lib64/camera/components/com.qti.node.swhme.so',
        'vendor/lib64/camera/components/com.qti.node.swlsc.so',
        'vendor/lib64/camera/components/com.qti.node.swmctf.so',
        'vendor/lib64/camera/components/com.qti.node.swregistration.so',
        'vendor/lib64/camera/components/com.qti.node.swvrt.so',
        'vendor/lib64/camera/components/com.qti.stats.aecwrapper.so',
        'vendor/lib64/camera/components/com.qti.stats.aecxcore.so',
        'vendor/lib64/camera/components/com.qti.stats.af.so',
        'vendor/lib64/camera/components/com.qti.stats.afc.so',
        'vendor/lib64/camera/components/com.qti.stats.afd.so',
        'vendor/lib64/camera/components/com.qti.stats.afwrapper.so',
        'vendor/lib64/camera/components/com.qti.stats.asd.so',
        'vendor/lib64/camera/components/com.qti.stats.awb.so',
        'vendor/lib64/camera/components/com.qti.stats.awbr.so',
        'vendor/lib64/camera/components/com.qti.stats.awbwrapper.so',
        'vendor/lib64/camera/components/com.qti.stats.cnndriver.so',
        'vendor/lib64/camera/components/com.qti.stats.exampleaf.so',
        'vendor/lib64/camera/components/com.qti.stats.haf.so',
        'vendor/lib64/camera/components/com.qti.stats.localhistogram.so',
        'vendor/lib64/camera/components/com.qti.stats.pdlib.so',
        'vendor/lib64/camera/components/com.qti.stats.pdlibwrapper.so',
        'vendor/lib64/camera/components/com.qti.stats.roimixer.so',
        'vendor/lib64/camera/components/com.qti.stats.roimixerlib.so',
        'vendor/lib64/camera/components/com.qti.stats.statsgenerator.so',
        'vendor/lib64/camera/components/com.qti.stats.tracker.so',
        'vendor/lib64/camera/components/libcamxevainterface.so',
        'vendor/lib64/camera/components/libdepthmapwrapper_itof.so',
        'vendor/lib64/camera/components/libdepthmapwrapper_secure.so',
        'vendor/lib64/com.qti.camx.chiiqutils.so',
        'vendor/lib64/com.qti.chifeaturecompatibility.so',
        'vendor/lib64/com.qti.chiusecaseselector.so',
        'vendor/lib64/com.qti.feature2.afbrckt.so',
        'vendor/lib64/com.qti.feature2.anchorsync.so',
        'vendor/lib64/com.qti.feature2.demux.so',
        'vendor/lib64/com.qti.feature2.derivedoffline.so',
        'vendor/lib64/com.qti.feature2.frc.so',
        'vendor/lib64/com.qti.feature2.fusion.so',
        'vendor/lib64/com.qti.feature2.generic.so',
        'vendor/lib64/com.qti.feature2.gs.sm8850.so',
        'vendor/lib64/com.qti.feature2.hdr.so',
        'vendor/lib64/com.qti.feature2.mcreprocrt.so',
        'vendor/lib64/com.qti.feature2.memcpy.so',
        'vendor/lib64/com.qti.feature2.metadataserializer.so',
        'vendor/lib64/com.qti.feature2.mfsr.so',
        'vendor/lib64/com.qti.feature2.mfsr.titan.so',
        'vendor/lib64/com.qti.feature2.ml.so',
        'vendor/lib64/com.qti.feature2.mux.so',
        'vendor/lib64/com.qti.feature2.qcfa.so',
        'vendor/lib64/com.qti.feature2.raw2yuvhdr.so',
        'vendor/lib64/com.qti.feature2.rawhdr.so',
        'vendor/lib64/com.qti.feature2.realtimeserializer.so',
        'vendor/lib64/com.qti.feature2.rt.so',
        'vendor/lib64/com.qti.feature2.rtmcx.so',
        'vendor/lib64/com.qti.feature2.rtpostproc.so',
        'vendor/lib64/com.qti.feature2.serializer.so',
        'vendor/lib64/com.qti.feature2.statsregeneration.so',
        'vendor/lib64/com.qti.feature2.stub.so',
        'vendor/lib64/com.qti.feature2.swmf.so',
        'vendor/lib64/com.qti.qseeutils.so',
        'vendor/lib64/com.qti.stats.common.so',
        'vendor/lib64/com.qti.stats.sotr.so',
        'vendor/lib64/com.qualcomm.mcx.distortionmapper.so',
        'vendor/lib64/com.qualcomm.mcx.linearmapper.so',
        'vendor/lib64/com.qualcomm.mcx.nonlinearmapper.so',
        'vendor/lib64/com.qualcomm.mcx.policy.mfl.so',
        'vendor/lib64/com.qualcomm.mcx.policy.sfl.so',
        'vendor/lib64/com.qualcomm.qti.mcx.usecase.extension.so',
        'vendor/lib64/hw/camera.qcom.sm8850.so',
        'vendor/lib64/hw/camera.qcom.so',
        'vendor/lib64/hw/com.qti.chi.offline.so',
        'vendor/lib64/hw/com.qti.chi.override.so',
        'vendor/lib64/libaidenoiser.so',
        'vendor/lib64/libaidenoiserv2.so',
        'vendor/lib64/libbitmlengine.so',
        'vendor/lib64/libbitmlenginev2.so',
        'vendor/lib64/libcamxhexlpservicebase.so',
        'vendor/lib64/libcamxhwlfrontend.so',
        'vendor/lib64/libcamxhwlipedriver.so',
        'vendor/lib64/libcamxhwnodecontext.so',
        'vendor/lib64/libcamxifestriping.so',
        'vendor/lib64/libcamxncsdatafactory.so',
        'vendor/lib64/libcamxofehwl.so',
        'vendor/lib64/libcamxofeswl.so',
        'vendor/lib64/libcamxqsatalgo.so',
        'vendor/lib64/libcamxswispiqmodule.so',
        'vendor/lib64/libcamxswlipedriver.so',
        'vendor/lib64/libcamxswprocessalgo.so',
        'vendor/lib64/libcamxtintlessalgo.so',
        'vendor/lib64/libcamxvppservicebase.so',
        'vendor/lib64/libchicore.so',
        'vendor/lib64/libchifeature2.so',
        'vendor/lib64/libchinodeevautils.so',
        'vendor/lib64/libchinodehmeutils.so',
        'vendor/lib64/libcom.qti.chinodeutils.so',
        'vendor/lib64/libdscaalgo.so',
        'vendor/lib64/libhme.so',
        'vendor/lib64/libhwliqinterface2.so',
        'vendor/lib64/libhwlispcffdump.so',
        'vendor/lib64/libipebpsstriping.so',
        'vendor/lib64/libipebpsstriping170.so',
        'vendor/lib64/libipebpsstriping480.so',
        'vendor/lib64/libisphwsetting.so',
        'vendor/lib64/libjpege.so',
        'vendor/lib64/libmctfengine_stub.so',
        'vendor/lib64/libmfec.so',
        'vendor/lib64/libmmcamera_bestats.so',
        'vendor/lib64/libmmcamera_cac.so',
        'vendor/lib64/libmmcamera_lscv35.so',
        'vendor/lib64/libmmcamera_mfnr.so',
        'vendor/lib64/libmmcamera_mfnr_t4.so',
        'vendor/lib64/libmmcamera_pdpc.so',
        'vendor/lib64/libofestriping.so',
        'vendor/lib64/libqfdadapter.so',
        'vendor/lib64/libqfdservice.so',
        'vendor/lib64/libsiminputgenutil.so',
        'vendor/lib64/libtfestriping.so',
        'vendor/lib64/libubifocus.so',
        'vendor/lib64/libvideoml.so',
        'vendor/lib64/vendor.qti.hardware.camera.aon-service-impl.so',
    ): blob_fixup()
        .remove_needed('libcamxsocketserverutil.so'),
    'odm/lib64/libEIS.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_acquire')
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'odm/lib64/libocam_hmbird.so': blob_fixup()
        .remove_needed('liboplus-uah-client.so'),
    'odm/lib64/liboprec_audrec.so': blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'odm/lib64/soundfx/libOplusSpatializerAidl.so': blob_fixup()
        .add_needed('libbase.so')
        .patch_file('blob-patches/libOplusSpatializerAidl.py'),
    'odm/vendor/etc/wifi/WCNSS_qcom_cfg.ini': blob_fixup()
        .regex_replace(r'(wlm_latency_flags_ultralow =)0x180d83', r'\g<1>0x180c82'),
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),
    'vendor/etc/vintf/manifest/vendor.qti.camera.offlinecamera-impl.xml': blob_fixup()
        .regex_replace('<version>2</version>', '<version>3</version>'),
    'vendor/lib64/camera/components/com.qti.node.dewarp.so': blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so')
        .remove_needed('libcamxsocketserverutil.so'),
    'vendor/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so': blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so')
        .replace_needed('vendor.qti.hardware.camera.offlinecamera-V2-ndk.so', 'vendor.qti.hardware.camera.offlinecamera-V3-ndk.so')
        .remove_needed('libcamxsocketserverutil.so'),
    (
        'vendor/lib64/camera/components/com.qti.node.fd.so',
        'vendor/lib64/hw/camera.qcom.core.so',
    ): blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so')
        .remove_needed('libcamxsocketserverutil.so'),
    'vendor/lib64/libcamxdumpinforecorder.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v36.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'infiniti',
    'oneplus',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

add_generated_thermal_engine_config(module)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8850-common', module.vendor
    )
    utils.run()
