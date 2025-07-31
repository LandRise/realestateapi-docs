---
title: Wordpress
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## WPGetAPI

[https://wpgetapi.com/downloads/pro-plugin/](https://wpgetapi.com/downloads/pro-plugin/)

For the simplest and least code solution, WPGetAPI provides a paid solution to pull data right into your UI.

![](https://files.readme.io/06502af-wordpressExample.png)

If you want to learn more about more advanced WordPress concepts relating to APIs, visit WP Engine's informative post on it: [https://wpengine.com/resources/using-wordpress-rest-api-plugin/](https://wpengine.com/resources/using-wordpress-rest-api-plugin/)

## For Wordpress Devs

Whether you have some wordpress savvy yourself or a team of wordpress devs, there are a few other options out there. 

[https://developer.wordpress.org/rest-api/](https://developer.wordpress.org/rest-api/)

[https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-custom-endpoints/](https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-custom-endpoints/)

A modified sample of the code provided at the bottom of that page would look something like:

```
<?php

class Slug_Custom_Route extends WP_REST_Controller {

  /**
   * Register the routes for the objects of the controller.
   */
  public function register_routes() {
    $version = '2'; //for property boundary, skiptrace, and Bulk Skiptrace use '1'
    $namespace = 'https://api.realestateapi.com/v' . $version;
    $base = 'route';
    register_rest_route( $namespace, '/PropertyDetail' . $base, array(
     array(
     	'methods'              => WP_REST_Server::READABLE,
      'callback'             => array( $this, 'runPropertyDetail' ),
      
     )
    ) );
    register_rest_route( $namespace, '/' . $base . '/(?P<id>[\d]+)', array(
      array(
        'methods'             => WP_REST_Server::READABLE,
        'callback'            => array( $this, 'get_item' ),
        'permission_callback' => array( $this, 'get_item_permissions_check' ),
        'args'                => array(
          'context' => array(
            'default' => 'view',
          ),
        ),
      )
    ) );
    register_rest_route( $namespace, '/' . $base . '/schema', array(
      'methods'  => WP_REST_Server::READABLE,
      'callback' => array( $this, 'get_public_item_schema' ),
    ) );
  }

  
  
  public function runPropertyDetail( $request ) {
    
    
    
  }

  

  /**
   * Create one item from the collection
   *
   * @param WP_REST_Request $request Full data about the request.
   * @return WP_Error|WP_REST_Response
   */
  public function create_item( $request ) {
    $item = $this->prepare_item_for_database( $request );

    if ( function_exists( 'slug_some_function_to_create_item' ) ) {
      $data = slug_some_function_to_create_item( $item );
      if ( is_array( $data ) ) {
        return new WP_REST_Response( $data, 200 );
      }
    }

    return new WP_Error( 'cant-create', __( 'message', 'text-domain' ), array( 'status' => 500 ) );
  }

 

  /**
   * Get the query params for collections
   *
   * @return array
   */
  public function get_collection_params() {
    return array(
      'page'     => array(
        'description'       => 'Current page of the collection.',
        'type'              => 'integer',
        'default'           => 1,
        'sanitize_callback' => 'absint',
      ),
      'per_page' => array(
        'description'       => 'Maximum number of items to be returned in result set.',
        'type'              => 'integer',
        'default'           => 10,
        'sanitize_callback' => 'absint',
      ),
      'search'   => array(
        'description'       => 'Limit results to those matching a string.',
        'type'              => 'string',
        'sanitize_callback' => 'sanitize_text_field',
      ),
    );
  }
}
```
