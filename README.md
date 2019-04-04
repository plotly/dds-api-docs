# Dash Deployment Server API Docs

These docs contain the reference DDS GraphQL API (found in the `.md` files), as well as runnable Python examples for each query and mutation.

## Running Python Examples

1. `pipenv install --dev`
2. `pipenv shell`
3. Update the `DDS_ENDPOINT` in [`dds.py`](./dds.py) to the deployment of DDS you are using
4. Run `python <path/to/example.py>`
   - Example: `python mutations/addApp/example.py`

## Auto-generating Reference Docs

1. Start DDS `server.py` on port `8888`
2. Run `npm install`
3. Run `npm run generate` to automatically generate the markdown reference files

**Note**: `npm run generate` will run the `genReferenceDocs.js` script for you.
