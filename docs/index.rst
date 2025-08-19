:og:description: LSSTCam is the camera for the Vera C. Rubin Observatory Legacy Survey of Space and Time (LSST).

#########################
The LSST Camera (LSSTCam)
#########################


*Citation:* SLAC National Accelerator Laboratory & NSF-DOE Vera C. Rubin Observatory, *The LSST Camera (LSSTCam)* (2025) |doi_image| https://doi.org/10.71929/rubin/2571927 [:download:`BibTeX <camera.bib>`]

The LSST Camera (LSSTCam) was mounted on the Simonyi Survey Telescope in `March 2025 <https://rubinobservatory.org/news/lsst-camera-installed>`_. LSSTCam will be used to take data for the `Legacy Survey of Space and Time <https://rubinobservatory.org/for-scientists/rubin-101/the-legacy-survey-of-space-and-time-lsst>`_ :cite:`2019ApJ...873..111I`.
It has 3.2 Gigapixels over a 9.6 square degree field of view and six optical filters.

.. image:: /lsstcam-on-telescope.jpg
   :width: 75%
   :alt: The camera mounted on the Simonyi Survey Telescope

Focal plane
===========

The LSST Camera focal plane is composed of 189 individual science charge-coupled devices (CCDs), arranged into 21 "rafts,"
along with 8 wavefront and 8 guider CCDs located in 4 additional corner rafts.
Each pixel is 0.2 arcseconds on the sky, and so each CCD of approximately 4,000 by 4,000 pixels covers 13.3 by 13.3 arcminutes (0.22 by 0.22 degrees).
Every CCD has 16 amplifiers, each reading 1 million pixels, enabling the full focal plane of of 3.2 Gigapixels to be read out in 2 seconds.

The CCDs were supplied by two vendors, `ITL <https://www.itl.arizona.edu/capabilities>`_ and `e2v <https://www.teledyne-e2v.com/en-us>`_.
All nine detectors in a given raft are from the same vendor.
Differences between sensors are accounted for during the Instrument Signature Removal (ISR)
stage of image processing :cite:p:`2025JATIS..11a1209P` by the LSST Science Pipelines :cite:p:`PSTN-019`.

.. figure:: /05_2025_rubin_focal_plane_final.jpg
   :name: lsstcam_focal_plane
   :alt: A visualization of the LSSTCam focal plane.

   Figure 1: A depiction of the focal plane of the LSST Camera.

Key numbers
===========

Except for the gap sizes, these numbers come from Table 6 of :cite:`SITCOMTN-148`.

* Inter-raft gap size (x, y) [mm]: 0.50, 0.50
* Inter-sensor gap size, (x, y) [mm]: 0.28, 0.25 (e2v); 0.27, 0.27 (ITL)
* Serial charge transfer inefficiency [%]: 7.3 e-6 (e2v); 1.5 e-4 (ITL)
* Parallel charge transfer inefficiency [%]: 1.1 e-5 (e2v); 1.2 e-6 (ITL)
* Dark current [e-/pix/s]: 0.023 (e2v); 0.021 (ITL)
* Photon Transfer Curve (PTC) turnoff [e-]: 103000 (e2v); 129000 (ITL)
* Read noise [e-]: 5.40 (e2v); 6.21 (ITL)
* Gain [e-/ADU]: 1.51 (e2v); 1.68 (ITL)


Components
==========

.. image:: /Camera_Exploded_View_labeled.jpg
   :width: 75%
   :alt: Exploded view of camera

.. image:: /shutter.webp
   :width: 50%
   :alt: view of the shutter


The shutter's two sides slide back and forth to expose and then cover the focal plane. The nominal shutter open/close time is 1 second.

.. image:: /filter_assembly.webp
   :width: 50%
   :alt: filter change mechanism

The filter changer mechanism - which holds 5 of the 6 LSST filters at a time - moves a filter in and out of the light path. The nominal filter change time is 2 minutes.

Filters
=======

The LSST's six filters are *u*, *g*, *r*, *i*, *z*, and *y*.
At any given time, five will be loaded into the camera's filter carousel, with a sixth filter swapped in every couple of weeks (depending on moon illumination, survey strategy, etc.).

For each filter, the effective wavelength -- defined as the mean wavelength by the system response in energy units -- and the full width at have maximum (FWHM) -- defined as the wavelength interval between the points where the system throughput drops to 50% of its peak value -- are shown in the following table.

+-------+--------------------+-------------+
| Band  | eff_wavelen (nm)   | fwhm (nm)   |
+=======+====================+=============+
| u     | 372.4              | 46.3        |
+-------+--------------------+-------------+
| g     | 480.7              | 148.5       |
+-------+--------------------+-------------+
| r     | 622.1              | 139.9       |
+-------+--------------------+-------------+
| i     | 755.9              | 128.6       |
+-------+--------------------+-------------+
| z     | 868.0              | 104.0       |
+-------+--------------------+-------------+
| y     | 975.3              | 86.2        |
+-------+--------------------+-------------+


The data for this table can be found `in the throughputs package <https://github.com/lsst/throughputs/tree/main/baseline>`_.


.. image:: /LSSTfilters_v1.9.png
   :width: 50%
   :alt: Lsst filters

Above, the filter transmission curves for the LSST Camera's six filters: u, g, r, i, z, and y.
These throuputs include atmospheric transmission (assuming an airmass of 1.2, dotted line), optics,
and the detector sensitivity.

Citing LSSTCam
==============

Use of the correct formal citation strings and keywords ensures that all uses of data from LSSTCam can be found using community tools.

* DOI: https://doi.org/10.71929/rubin/2571927 (refers to this document)

  * Use this DOI when referring to the instrument specifically; otherwise a dataset DOI may be more appropriate (see the documentation for the specific data release you are using) or a technical reference such as Roodman et al. (2024) given below.

* IVOA `ObsCore <https://www.ivoa.net/documents/ObsCore/20170509/index.html>`_ keywords: ``facility_name`` = ``Rubin:Simonyi``, ``instrument_name`` = ``LSSTCam``
* AAS `facility keyword <https://journals.aas.org/facility-keywords/>`_: ``Rubin:Simonyi`` or, for specificity, ``Rubin:Simonyi (LSSTCam)``
* Minor Planet Center `observatory code <https://minorplanetcenter.net/iau/lists/ObsCodesF.html>`_: ``X05``


Technical Documentation
=======================

* `LSST Camera verification testing and characterization <https://ui.adsabs.harvard.edu/abs/2024SPIE13096E..1SR/abstract>`_, Roodman et al. (2024; SPIE, `doi:10.1117/12.3019698 <https://doi.org/10.1117/12.3019698>`_)
* `LSST Camera focal plane optimization <https://ui.adsabs.harvard.edu/abs/2024SPIE13103E..0WU/abstract>`_, Utsumi et al. (2024; SPIE, `doi:10.1117/12.3019117 <https://doi.org/10.1117/12.3019117>`_)
* `Integrating the LSST camera <https://ui.adsabs.harvard.edu/abs/2024SPIE13096E..1OL/abstract>`_, Lange et al. (2024; SPIE `doi:10.1117/12.3019302 <https://doi.org/10.1117/12.3019302>`_)
* `LSST Camera Electro-Optical Test (Run 7) Results <https://sitcomtn-148.lsst.io>`_, Antilogus et al. (2025, NSF-DOE Vera C. Rubin Observatory Commissioning Technical Note 148)
* `Design and development of the 3.2 gigapixel camera for the Large Synoptic Survey Telescope <https://ui.adsabs.harvard.edu/abs/2010SPIE.7735E..0JK/abstract>`_, Kahn et al. (2010; SPIE, `doi:10.1117/12.857920 <https://doi.org/10.1117/12.857920>`_)
* `The LSST camera overview: design and performance <https://ui.adsabs.harvard.edu/abs/2008SPIE.7014E..0CG/abstract>`_, Gilmore et al. (2008; SPIE, `doi:10.1117/12.789947 <https://doi.org/10.1117/12.789947>`_)
* `The LSST Camera system overview <https://ui.adsabs.harvard.edu/abs/2006SPIE.6269E..0CG/abstract>`_, Gilmore et al. (2006; SPIE, `doi:10.1117/12.673236 <https://doi.org/10.1117/12.673236>`_)
* `LCA-13381: Detector Plane Layout <https://zenodo.org/records/15133467>`_ , M. Nordby, 2020
* `LSSTCam and LSSTComCam Focal Plane Layouts <https://doi.org/10.5281/zenodo.15133467>`_, Plazas Malagón et al., (NSF-DOE Vera C. Rubin Observatory Camera Technical Note 001)

References
==========

.. bibliography::
