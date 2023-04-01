import json
from picterra import APIClient


class Picterra_detection:

    detector_id=""
    def tranning(self, file='data/raster1.tif'):

        client = APIClient()
        self.detector_id = client.create_detector('Object detector')
        raster_id = client.upload_raster(file, name='Object detection raster')
        client.add_raster_to_detector(raster_id, self.detector_id)

        # Add annotations
        with open('data/outline.geojson') as f:
            outlines = json.load(f)
        client.set_annotations(self.detector_id, raster_id, 'outline', outlines)

        with open('data/training_area.geojson') as f:
            training_areas = json.load(f)
        client.set_annotations(self.detector_id, raster_id, 'training_area', training_areas)

        with open('data/validation_area.geojson') as f:
            validation_areas = json.load(f)
        client.set_annotations(self.detector_id, raster_id, 'validation_area', validation_areas)

        # Train the detector
        client.train_detector(self.detector_id)

        print(self.detector_id)

    def detection(self, file="data/palmier_extrait.tif"):

        detector_id = "1ac95439-d41c-4b1b-9b02-bc0738b417a8" #1958d078-f0df-44dd-9915-22f58bb378da
        folder_id = "2ff2d9f0-7f6a-49ed-84df-ea7a4693bc4a" # #3bb51a6c-3ee7-431b-8217-c12b4e899efd
        client = APIClient()

        print('Uploading raster...')
        raster_id = client.upload_raster(
            file,
            name='Object detection',
            folder_id=folder_id
        )

        print('Upload finished, starting detector...')
        result_id = client.run_detector(detector_id, raster_id)
        result = client.download_result_to_feature_collection(result_id, 'data/object_result.geojson')

        print('Detection finished, results are in object_result.geojson')

