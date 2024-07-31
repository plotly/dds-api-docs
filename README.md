# Dash Enterprise API Docs

These docs contain the reference DDS GraphQL API (found in the `.md` files), as well as runnable Python examples for each query and mutation.

<div align="center">
  <a href="https://dash.plotly.com/project-maintenance">
    <img src="https://dash.plotly.com/assets/images/maintained-by-plotly.png" width="400px" alt="Maintained by Plotly">
  </a>
</div>

## Running Python Examples

1. `pipenv install --dev`
2. `pipenv shell`
3. Update the variables at the top of [`dds.py`](./dds.py) to match your DDS settings.

    ```shell
    export DDS_DOMAIN_NAME="dash.example.com"
    export DDS_USERNAME="username"
    export DDS_API_KEY="api_key"
    ```

4. Run `python <path/to/example.py>`
   - Example: `python queries/apps/by_page.py`

## Auto-generating Reference Docs

1. Export the `DDS_DOMAIN_NAME` environment variable
2. Run `npm install`
3. Run `npm run generate` to automatically generate the markdown reference files

**Note**: `npm run generate` will run the `genReferenceDocs.js` script for you.
